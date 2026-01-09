#!/usr/bin/env python3
"""
Sync Obsidian blog posts to Hugo content directory.

MIN-148: Core file processing (title extraction, frontmatter generation)
MIN-149: Wikilink conversion (to be added)
MIN-150: Image handling (to be added)
"""

import os
import re
import shutil
from datetime import datetime
from pathlib import Path

# Configuration
OBSIDIAN_BLOG_DIR = Path("/Users/minjaekwon1/Documents/Obsidian Vault/blog")
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


def process_file(source_path: Path) -> dict:
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

    # Generate frontmatter
    frontmatter = generate_frontmatter(title, date)

    # Combine frontmatter and content
    output_content = frontmatter + content

    return {
        'status': 'success',
        'title': title,
        'slug': slug,
        'content': output_content,
        'source': source_path
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

    synced = 0
    skipped = 0

    for source_path in md_files:
        result = process_file(source_path)

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

        print(f"  SYNC: {source_path.name} -> {result['slug']}/index.md")
        synced += 1

    print("-" * 50)
    print(f"Done. Synced: {synced}, Skipped: {skipped}")


if __name__ == '__main__':
    sync_posts()
