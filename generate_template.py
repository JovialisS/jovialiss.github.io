#!/usr/bin/env python3
"""
扫描 _posts，生成 _data/title_slugs.yml 模板。
已有 slug 的文章会自动跳过。
"""

import re
import sys
from pathlib import Path

POSTS_DIR = "_posts"
OUTPUT = "_data/title_slugs.yml"


def extract_title(filepath: Path) -> str | None:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    fm = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not fm:
        return None
    front_matter = fm.group(1)
    if re.search(r"^slug\s*:", front_matter, re.MULTILINE):
        return None  # 已有 slug，跳过
    m = re.search(r"^title\s*:\s*(.+)", front_matter, re.MULTILINE)
    if not m:
        return None
    return m.group(1).strip().strip("'\"")


def main():
    posts = Path(POSTS_DIR)
    if not posts.exists():
        print("错误：找不到 _posts 目录")
        sys.exit(1)

    titles = []
    for f in sorted(posts.glob("*.md")):
        t = extract_title(f)
        if t:
            titles.append(t)

    if not titles:
        print("所有文章都已有 slug，无需生成。")
        return

    Path("_data").mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write("# 中文标题: 英文小驼峰slug（请手动填写右侧）\n")
        for t in titles:
            f.write(f"{t}: \n")

    print(f"已生成 {OUTPUT}，共 {len(titles)} 篇文章待填写 slug。")
    print("填完后运行 apply_slugs.py 批量写入。")


if __name__ == "__main__":
    main()