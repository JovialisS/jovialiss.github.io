#!/usr/bin/env python3
"""
读取 _data/title_slugs.yml，把英文小驼峰 slug 写入文章 Front Matter。
"""

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("请先安装：pip install pyyaml")
    sys.exit(1)

POSTS_DIR = "_posts"
SLUG_MAP_FILE = "_data/title_slugs.yml"
SLUG_FIELD = "slug"


def to_camel(text: str) -> str:
    words = re.split(r"[\s\-_]+", text)
    if not words:
        return ""
    return words[0].lower() + "".join(w.capitalize() for w in words[1:])


def load_map() -> dict:
    p = Path(SLUG_MAP_FILE)
    if not p.exists():
        print(f"找不到 {SLUG_MAP_FILE}")
        sys.exit(1)
    with open(p, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data if isinstance(data, dict) else {}


def process_file(filepath: Path, slug_map: dict) -> bool:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    fm = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not fm:
        return False
    front_matter = fm.group(1)
    body = content[fm.end():]
    if re.search(rf"^{SLUG_FIELD}\s*:", front_matter, re.MULTILINE):
        return False
    m = re.search(r"^title\s*:\s*(.+)", front_matter, re.MULTILINE)
    if not m:
        return False
    title = m.group(1).strip().strip("'\"")
    slug = slug_map.get(title)
    if not slug or not slug.strip():
        print(f"  [未填写] {filepath.name} → 「{title}」")
        return False
    slug = to_camel(slug.strip())
    new_fm = re.sub(
        r"(^title\s*:.+)",
        rf"\1\n{SLUG_FIELD}: {slug}",
        front_matter,
        count=1,
        flags=re.MULTILINE,
    )
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("---\n" + new_fm + "\n---\n" + body)
    print(f"  [写入] {filepath.name} → {slug}")
    return True


def main():
    slug_map = load_map()
    modified = 0
    for f in sorted(Path(POSTS_DIR).glob("*.md")):
        if process_file(f, slug_map):
            modified += 1
    print(f"\n完成，写入 {modified} 篇。")


if __name__ == "__main__":
    main()