#!/usr/bin/env python3
"""
Sync Obsidian blog posts to Hugo content directory.

MIN-148: Core file processing (title extraction, frontmatter generation)
MIN-149: Wikilink conversion
MIN-150: Image handling
"""

import os
import re
import shutil
from datetime import datetime
from pathlib import Path
from typing import Optional

# Configuration
OBSIDIAN_BLOG_DIR = Path("/Users/minjaekwon1/Projects/obsidian/blog")
HUGO_CONTENT_DIR = Path("/Users/minjaekwon1/Projects/lminsl.github.io/content/blog")
HUGO_IMAGES_DIR = Path("/Users/minjaekwon1/Projects/lminsl.github.io/static/images/blog")


def slugify(text: str) -> str:
    """Convert text to URL-friendly slug."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')


def extract_title(content: str, filename: str) -> str:
    """Extract title from first H1 heading or use filename."""
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return filename.replace('.md', '').replace('-', ' ').title()


def remove_title_heading(content: str) -> str:
    """Remove the first H1 heading from content (it becomes the title)."""
    return re.sub(r'^#\s+.+\n*', '', content, count=1, flags=re.MULTILINE)


def convert_wikilinks(content: str, existing_slugs: set) -> str:
    """Convert Obsidian wikilinks to standard markdown links.

    [[note]] → [note](/blog/note/) if note exists, else just "note"
    [[note|alias]] → [alias](/blog/note/) if note exists, else just "alias"
    """
    def replace_wikilink(match):
        inner = match.group(1)

        if '|' in inner:
            path, alias = inner.split('|', 1)
        else:
            path = inner
            alias = None

        # Extract note name from path (last segment)
        note_name = path.split('/')[-1]

        # Clean up note name (remove any file extension)
        if note_name.endswith('.md'):
            note_name = note_name[:-3]

        # Use alias if provided, otherwise use note name
        display_text = alias if alias else note_name

        # Create slug for the link
        link_slug = slugify(note_name)

        # Only create link if target post exists
        if link_slug in existing_slugs:
            return f'[{display_text}](/blog/{link_slug}/)'
        else:
            return display_text  # Plain text, no link

    # Match [[...]] but not ![[...]] (images handled separately)
    return re.sub(r'(?<!!)\[\[([^\]]+)\]\]', replace_wikilink, content)


def find_image(image_name: str, search_dirs: list) -> Optional[Path]:
    """Search for an image file in multiple directories."""
    for search_dir in search_dirs:
        if not search_dir.exists():
            continue

        # Direct match in directory
        candidate = search_dir / image_name
        if candidate.exists():
            return candidate

        # Search recursively
        for match in search_dir.rglob(image_name):
            return match

    return None


def process_images(content: str, source_path: Path) -> tuple[str, list[Path]]:
    """Process image embeds: convert syntax and collect images to copy.

    ![[image.png]] → ![image](/images/blog/image.png)
    """
    images_to_copy = []
    vault_root = OBSIDIAN_BLOG_DIR.parent
    search_dirs = [
        source_path.parent,  # Same folder as the note
        OBSIDIAN_BLOG_DIR,   # Blog folder
        vault_root / 'attachments',  # Common attachments folder
        vault_root,          # Vault root (recursive search last)
    ]

    def replace_image(match):
        image_ref = match.group(1)

        # Handle path in image reference
        image_name = image_ref.split('/')[-1]

        # Remove any alias (e.g., ![[image.png|300]])
        if '|' in image_name:
            image_name = image_name.split('|')[0]

        # Find the image file
        image_path = find_image(image_name, search_dirs)

        if image_path:
            images_to_copy.append(image_path)
            # Generate alt text from filename (without extension)
            alt_text = image_name.rsplit('.', 1)[0]
            return f'![{alt_text}](/images/blog/{image_name})'
        else:
            print(f"  WARNING: Image not found: {image_name}")
            # Return broken image marker so it's visible
            return f'![MISSING: {image_name}](/images/blog/{image_name})'

    # Match ![[...]] image embeds
    converted = re.sub(r'!\[\[([^\]]+)\]\]', replace_image, content)

    return converted, images_to_copy


def copy_images(images: list[Path]) -> int:
    """Copy images to Hugo static directory."""
    copied = 0
    for image_path in images:
        dest = HUGO_IMAGES_DIR / image_path.name
        if not dest.exists() or image_path.stat().st_mtime > dest.stat().st_mtime:
            shutil.copy2(image_path, dest)
            copied += 1
    return copied


def get_file_date(filepath: Path) -> str:
    """Get file modification date in ISO format."""
    mtime = os.path.getmtime(filepath)
    dt = datetime.fromtimestamp(mtime)
    return dt.strftime('%Y-%m-%dT%H:%M:%S+09:00')


def generate_frontmatter(title: str, date: str, draft: bool = False) -> str:
    """Generate Hugo frontmatter."""
    return f"""---
title: "{title}"
date: {date}
draft: {str(draft).lower()}
---

"""


def get_all_slugs(md_files: list) -> set:
    """Pre-scan all files to get their slugs."""
    slugs = set()
    for source_path in md_files:
        if source_path.name.startswith('_'):
            continue
        content = source_path.read_text(encoding='utf-8')
        title = extract_title(content, source_path.name)
        slugs.add(slugify(title))
    return slugs


def process_file(source_path: Path, existing_slugs: set) -> dict:
    """Process a single Obsidian markdown file."""
    content = source_path.read_text(encoding='utf-8')
    filename = source_path.name

    # Skip files starting with underscore (drafts)
    if filename.startswith('_'):
        return {'status': 'skipped', 'reason': 'draft file'}

    # Extract metadata
    title = extract_title(content, filename)
    slug = slugify(title)
    date = get_file_date(source_path)

    # Remove title heading from content (will be in frontmatter)
    content = remove_title_heading(content)

    # Convert wikilinks to standard markdown (only link to existing posts)
    content = convert_wikilinks(content, existing_slugs)

    # Process images (convert syntax and collect images to copy)
    content, images = process_images(content, source_path)

    # Generate frontmatter
    frontmatter = generate_frontmatter(title, date)

    # Combine frontmatter and content
    output_content = frontmatter + content

    return {
        'status': 'success',
        'title': title,
        'slug': slug,
        'content': output_content,
        'source': source_path,
        'images': images
    }


def sync_posts():
    """Main sync function."""
    print(f"Syncing from: {OBSIDIAN_BLOG_DIR}")
    print(f"Syncing to: {HUGO_CONTENT_DIR}")
    print("-" * 50)

    # Ensure output directories exist
    HUGO_CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    HUGO_IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    # Find all markdown files
    md_files = list(OBSIDIAN_BLOG_DIR.glob('*.md'))

    if not md_files:
        print("No markdown files found in blog folder.")
        return

    # Pre-scan to get all slugs (for smart linking)
    existing_slugs = get_all_slugs(md_files)
    print(f"Found {len(existing_slugs)} posts to sync")

    synced = 0
    skipped = 0
    images_copied = 0

    for source_path in md_files:
        result = process_file(source_path, existing_slugs)

        if result['status'] == 'skipped':
            print(f"  SKIP: {source_path.name} ({result['reason']})")
            skipped += 1
            continue

        # Create output directory
        output_dir = HUGO_CONTENT_DIR / result['slug']
        output_dir.mkdir(parents=True, exist_ok=True)

        # Write output file
        output_path = output_dir / 'index.md'
        output_path.write_text(result['content'], encoding='utf-8')

        # Copy images
        if result['images']:
            copied = copy_images(result['images'])
            images_copied += copied

        print(f"  SYNC: {source_path.name} -> {result['slug']}/index.md")
        synced += 1

    print("-" * 50)
    print(f"Done. Synced: {synced}, Skipped: {skipped}, Images: {images_copied}")


if __name__ == '__main__':
    sync_posts()
