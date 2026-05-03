import os
import re

# パスの設定
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ATCODER_DIR = os.path.join(BASE_DIR, "AtCoder")
README_PATH = os.path.join(BASE_DIR, "README.md")

START_MARKER = "<!-- DASHBOARD_START -->"
END_MARKER = "<!-- DASHBOARD_END -->"

def get_status(readme_path):
    """READMEの中身を詳細に読み取ってステータスを判定する"""
    if not os.path.exists(readme_path):
        return "未"
    
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
        
        # チェックボックスの状態を判定
        # [x] か [X] がついている行を探し、その直後のキーワードで判別
        if re.search(r"\[[xX]\]\s*✅\s*自力AC", content):
            return "⭕️"
        elif re.search(r"\[[xX]\]\s*📖\s*解説AC", content):
            return "📖"
        elif re.search(r"\[[xX]\]\s*🧪\s*実装のみ参考", content):
            return "🧪"
        else:
            return "未"

def generate_dashboard():
    """アコーディオン形式のダッシュボードを生成"""
    # 凡例の追加（PdM視点での状況把握を容易にするため）
    lines = [
        "\n### 🟢 AtCoder Beginner Contest (ABC)\n",
        "**凡例:** ⭕️ 自力AC | 📖 解説AC | 🧪 実装参考 | 未 着手前\n\n"
    ]
    
    if not os.path.exists(ATCODER_DIR):
        return "".join(lines)

    contests = sorted(
        [d for d in os.listdir(ATCODER_DIR) if d.startswith("abc")], 
        reverse=True
    )

    for contest in contests:
        contest_path = os.path.join(ATCODER_DIR, contest)
        problems = sorted([d for d in os.listdir(contest_path) if os.path.isdir(os.path.join(contest_path, d))])
        
        if not problems:
            continue

        lines.append(f"<details>\n<summary>{contest} (クリックで展開)</summary>\n\n")
        lines.append("| 問題 | 状態 | リンク |\n")
        lines.append("| :--- | :---: | :--- |\n")

        for problem in problems:
            readme_path = os.path.join(contest_path, problem, "README.md")
            status = get_status(readme_path)
            link = f"./AtCoder/{contest}/{problem}"
            lines.append(f"| {problem} | {status} | [Link]({link}) |\n")
            
        lines.append("\n</details>\n")

    return "".join(lines)

def update_readme():
    """README.mdのマーカー間を置換"""
    if not os.path.exists(README_PATH):
        print("README.mdが見つかりません。")
        return

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(rf"{START_MARKER}.*?{END_MARKER}", re.DOTALL)
    new_dashboard = f"{START_MARKER}\n{generate_dashboard()}\n{END_MARKER}"
    
    if pattern.search(content):
        new_content = pattern.sub(new_dashboard, content)
    else:
        new_content = content + f"\n\n{new_dashboard}"

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print("ダッシュボードを更新しました！")

if __name__ == "__main__":
    update_readme()