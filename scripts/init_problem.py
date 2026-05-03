# scripts/init_problem.py
import sys
import os
import json
import requests
from bs4 import BeautifulSoup

def fetch_problem_statement(url):
    """AtCoderのURLから問題文セクションを抽出する"""
    try:
        response = requests.get(url, timeout=5)
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text, 'html.parser')
        
        statement_div = soup.find('div', id='task-statement')
        if not statement_div:
            return "問題文を取得できませんでした。"
        
        # 日本語セクション（通常最初のsection）を取得
        first_section = statement_div.find('section')
        if first_section:
            if first_section.h3:
                first_section.h3.decompose()
            
            # 1. まず全体のテキストを結合して取得
            text = first_section.get_text(strip=True)
            
            # 2. 「。」を「。\n\n」に置換して、一文ごとに段落を分ける
            formatted_text = text.replace("。", "。\n\n")
            
            return formatted_text
            
        return "問題文が見つかりませんでした。"
    except Exception as e:
        return f"取得エラー: {e}"

def main():
    if len(sys.argv) < 2:
        return
    
    code_path = sys.argv[1]
    if os.path.isdir(code_path):
        problem_dir = code_path
    else:
        problem_dir = os.path.dirname(code_path)

    metadata_path = os.path.join(problem_dir, "metadata.json")
    readme_path = os.path.join(problem_dir, "README.md")

    if not os.path.exists(metadata_path):
        return

    with open(metadata_path, "r", encoding="utf-8") as f:
        meta = json.load(f)

    prob = meta.get("problem", {})
    alphabet = prob.get("alphabet", "---")
    problem_id = prob.get("problem_id", "---")
    contest_id = prob.get("contest", {}).get("contest_id", "")
    actual_url = f"https://atcoder.jp/contests/{contest_id}/tasks/{problem_id}"

    # 問題文を取得
    print(f"Fetching statement for {alphabet}...")
    statement_text = fetch_problem_statement(actual_url)

    content = f"""# {alphabet} - {problem_id}

- **URL:** {actual_url}
- **難易度:** {alphabet}

## 問題文
{statement_text}

---

## 解答ステータス
- [ ] ✅ 自力AC
- [ ] 📖 解説AC（復習が必要）
- [ ] 🧪 実装のみ参考（ロジックは自力）

## 考察・学んだこと
- 

## 関連アルゴリズム
- 
"""

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Generated README with statement for Problem {alphabet}")

if __name__ == "__main__":
    main()