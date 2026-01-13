# Obsidian Blog Setup (2026-01-10)

## Overview

Obsidian 노트를 Hugo 블로그로 자동 동기화하는 시스템 구축.

## 구조

```
~/Projects/obsidian/blog/          # 발행할 노트 복사
        ↓ (python3 scripts/sync-obsidian.py)
~/Projects/lminsl.github.io/
├── content/blog/{slug}/index.md   # 생성된 포스트
├── static/images/blog/            # 복사된 이미지
└── scripts/sync-obsidian.py       # 동기화 스크립트
```

## 사용법

### 1. 노트 발행하기
```bash
# Obsidian에서 발행할 노트를 blog 폴더로 복사 (원본 유지)
cp "~/Projects/obsidian/내노트.md" "~/Projects/obsidian/blog/"
```

### 2. 동기화 실행
```bash
cd ~/Projects/lminsl.github.io
python3 scripts/sync-obsidian.py
```

### 3. 배포
```bash
git add . && git commit -m "Add new post" && git push
```

### Claude Command
```
/sync-blog
```

## 변환 규칙

| Obsidian | Hugo |
|----------|------|
| `# 제목` (첫 H1) | frontmatter title |
| `[[노트\|표시텍스트]]` | `[표시텍스트](/blog/노트/)` (존재시만 링크) |
| `![[이미지.png]]` | `![이미지](/images/blog/이미지.png)` |
| 파일 수정일 | frontmatter date |
| `_초안.md` (밑줄) | 스킵됨 |

## 스마트 위키링크

- 블로그 폴더에 존재하는 노트만 링크 생성
- 없는 노트는 일반 텍스트로 표시 (404 방지)
- 나중에 해당 노트 추가 후 재동기화하면 자동으로 링크 생성

## 파일 위치

| 파일 | 용도 |
|------|------|
| `scripts/sync-obsidian.py` | 동기화 스크립트 |
| `scripts/README.md` | 스크립트 문서 |
| `layouts/blog/list.html` | 블로그 목록 템플릿 |
| `~/.claude/commands/sync-blog.md` | Claude 커맨드 |

## Linear Issues (완료됨)

- MIN-146: Obsidian blog 폴더 구조
- MIN-147: Hugo blog 섹션 추가
- MIN-148: 동기화 스크립트 코어
- MIN-149: 위키링크 변환
- MIN-150: 이미지 처리
- MIN-151: E2E 테스트
- MIN-152: README 작성

## 남은 작업 (Optional)

- [ ] 블로그 포스트 템플릿 개선 (날짜 표시, back link)
- [ ] 테스트 포스트 삭제 (실제 포스트 작성 후)
- [ ] SEO 메타 태그 개선

## Git Commits (오늘)

```
6974bde - Add Blog to homepage navigation
53872dd - Remove bawi post
dda00ec - Add bawi 첫 글 post, update README paths
4bb1193 - Smart wikilinks: only link to existing posts
c1fbed6 - Add README for Obsidian sync workflow (MIN-152)
c474287 - Add image handling to sync script (MIN-150)
76dba0d - Add wikilink conversion to sync script (MIN-149)
02429e0 - Add sync-obsidian.py script (MIN-148)
de3998a - Add blog section for Obsidian sync (MIN-147)
```

## 라이브 사이트

- 홈: https://lminsl.github.io/
- 블로그: https://lminsl.github.io/blog/
- RSS: https://lminsl.github.io/blog/index.xml
