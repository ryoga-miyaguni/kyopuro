#!/usr/bin/env python3
"""
競プロのREADME + コードからZenn記事ドラフトを生成するスクリプト

使い方:
  python scripts/generate_zenn_draft.py abc457 C
"""

import sys
import os
import json


def load_problem_data(contest: str, problem: str) -> dict:
    base = os.path.join(os.path.dirname(__file__), "..", "AtCoder", contest, problem)
    base = os.path.abspath(base)

    readme_path = os.path.join(base, "README.md")
    with open(readme_path, encoding="utf-8") as f:
        readme = f.read()

    meta_path = os.path.join(base, "metadata.json")
    code = ""
    lang = "python"
    if os.path.exists(meta_path):
        with open(meta_path, encoding="utf-8") as f:
            meta = json.load(f)
        code_file = os.path.join(base, meta.get("code_filename", "main.py"))
        lang = meta.get("lang", "python")
        if os.path.exists(code_file):
            with open(code_file, encoding="utf-8") as f:
                code = f.read()

    return {"readme": readme, "code": code, "lang": lang, "contest": contest, "problem": problem}


def parse_readme(readme: str) -> dict:
    lines = readme.splitlines()
    data = {"url": "", "status": "", "considerations": [], "algorithms": []}

    section = None
    for line in lines:
        if "URL:" in line:
            raw = line.split("URL:")[-1].strip()
            # "** https://..." のような装飾を除去
            data["url"] = raw.lstrip("* ").strip()
        elif "自力AC" in line and "[x]" in line:
            data["status"] = "自力AC"
        elif "解説AC" in line and "[x]" in line:
            data["status"] = "解説AC（復習あり）"
        elif "実装のみ参考" in line and "[x]" in line:
            data["status"] = "実装参考"
        elif "考察・学んだこと" in line:
            section = "considerations"
        elif "関連アルゴリズム" in line:
            section = "algorithms"
        elif section == "considerations" and line.startswith("- ") and line.strip() != "- ":
            data["considerations"].append(line.strip("- ").strip())
        elif section == "algorithms" and line.startswith("- ") and line.strip() != "- ":
            data["algorithms"].append(line.strip("- ").strip())

    return data


def generate_article(data: dict) -> str:
    contest = data["contest"].upper()
    problem = data["problem"]
    parsed = parse_readme(data["readme"])
    url = parsed["url"]
    status = parsed["status"] or "解説AC"
    considerations = parsed["considerations"]
    algorithms = parsed["algorithms"]
    code = data["code"]
    lang = data["lang"]

    title_hint = considerations[0][:25] if considerations else "解法メモ"

    article = f"""---
title: "[{contest}-{problem}] {title_hint}"
emoji: "📝"
type: "tech"
topics: ["atcoder", "競技プログラミング", "python", "アルゴリズム"]
published: false
---

## 問題

[{contest}-{problem} を AtCoder で見る]({url})

ステータス: **{status}**

---

## 考察・詰まったところ

"""

    for c in considerations:
        article += f"- {c}\n"

    article += f"""
:::message
ここに自分の言葉で一言補足を書くと読者に伝わりやすくなります
:::

---

## AC コード

```{lang}
{code.strip()}
```

---

## まとめ・学んだこと

"""

    if algorithms:
        article += "今回使ったアルゴリズム・考え方:\n\n"
        for alg in algorithms:
            article += f"- {alg}\n"
    else:
        article += "<!-- 使ったアルゴリズム・パターンをここに書く -->\n"

    base_url = url.rsplit("/tasks", 1)[0] if "/tasks" in url else url
    article += f"""
---

*AtCoder [{contest}]({base_url}) の振り返りメモです。同じところで詰まった人の参考になれば。*
"""
    return article


def main():
    if len(sys.argv) < 3:
        print("使い方: python scripts/generate_zenn_draft.py <contest> <problem>")
        print("例:     python scripts/generate_zenn_draft.py abc457 C")
        sys.exit(1)

    contest = sys.argv[1].lower()
    problem = sys.argv[2].upper()

    data = load_problem_data(contest, problem)
    article = generate_article(data)

    out_dir = os.path.join(os.path.dirname(__file__), "..", "zenn_drafts")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{contest}_{problem}.md")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(article)

    print(f"✅ ドラフト生成完了: {out_path}")


if __name__ == "__main__":
    main()
