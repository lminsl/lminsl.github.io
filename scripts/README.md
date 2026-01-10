# Obsidian to Hugo Sync

Syncs blog posts from Obsidian vault to Hugo content directory.

## Quick Start

```bash
# Run sync
python3 scripts/sync-obsidian.py

# Preview locally
hugo serve
```

## Workflow

1. **Copy** note to `~/Projects/obsidian/blog/` (keeps original in vault)
2. **Sync** with `python3 scripts/sync-obsidian.py`
3. **Commit** and push to deploy

## What Gets Transformed

| Obsidian | Hugo |
|----------|------|
| `# Title` (H1) | `title:` in frontmatter |
| `[[note\|alias]]` | `[alias](/blog/note/)` |
| `![[image.png]]` | `![image](/images/blog/image.png)` |
| File mtime | `date:` in frontmatter |

## Directory Structure

```
~/Projects/obsidian/
└── blog/
    ├── my-post.md          # Copied here to publish
    ├── _draft.md           # Skipped (underscore prefix)
    └── image.png           # Images

Hugo Project/
├── content/blog/
│   └── my-post/
│       └── index.md        # Generated post
├── static/images/blog/
│   └── image.png           # Copied images
└── scripts/
    └── sync-obsidian.py    # This script
```

## Post Format

```markdown
# My Post Title

Content here. Use Obsidian wikilinks:
- [[other-note]]
- [[path/to/note|display text]]

Images work too:
![[screenshot.png]]
```

**Note:** The first H1 becomes the title and is removed from content.

## Draft Posts

Prefix filename with underscore to skip:
- `_work-in-progress.md` → skipped
- `my-published-post.md` → synced

## Images

Images are searched in order:
1. Same folder as the post
2. Blog folder
3. `attachments/` folder
4. Entire vault (recursive)

Missing images show warning but don't stop sync.

## Claude Command

Run `/sync-blog` in Claude Code to execute the sync workflow.
