import os
import re

# パスの設定 (kyopuroフォルダを基準にする)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ATCODER_DIR = os.path.join(BASE_DIR, "AtCoder")
README_PATH = os.path.join(BASE_DIR, "README.md")

# README内の更新範囲を示すマーカー（目印）
START_MARKER = "<!-- DASHBOARD_START -->"
END_MARKER = "<!-- DASHBOARD_END -->"

def get_status(readme_path):
    """READMEの中身を読んでステータスを判定する"""
    if not os.path.exists(readme_path):
        return "未"
    
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
        # [x] か [X] が含まれていればAC（正解）とみなす
        if "[x]" in content or "[X]" in content:
            return "⭕️"
        else:
            # 何もついていなければ「未」
            return "未"

def generate_dashboard():
    """ダッシュボードのMarkdown文字列を生成する"""
    lines = ["\n### 🟢 AtCoder Beginner Contest (ABC)\n"]
    
    if not os.path.exists(ATCODER_DIR):
        return "".join(lines)

    # abcXXX のようなフォルダを取得し、最新のコンテストが上に来るように降順ソート
    contests = sorted(
        [d for d in os.listdir(ATCODER_DIR) if d.startswith("abc")], 
        reverse=True
    )

    for contest in contests:
        contest_path = os.path.join(ATCODER_DIR, contest)
        # A, B, C... のフォルダを取得してアルファベット順にソート
        problems = sorted([d for d in os.listdir(contest_path) if os.path.isdir(os.path.join(contest_path, d))])
        
        if not problems:
            continue

        # 折りたたみ（アコーディオン）の開始
        lines.append(f"<details>\n<summary>{contest} (クリックで展開)</summary>\n\n")
        lines.append("| 問題 | ステータス | リンク |\n")
        lines.append("| :--- | :---: | :--- |\n")

        for problem in problems:
            problem_path = os.path.join(contest_path, problem)
            readme_path = os.path.join(problem_path, "README.md")
            
            # ステータスを取得して行を作成
            status = get_status(readme_path)
            link = f"./AtCoder/{contest}/{problem}"
            
            lines.append(f"| {problem} | {status} | [Link]({link}) |\n")
            
        # 折りたたみの終了
        lines.append("\n</details>\n")

    return "".join(lines)

def update_readme():
    """ルートのREADME.mdを更新する"""
    if not os.path.exists(README_PATH):
        print(f"エラー: {README_PATH} が見つかりません。")
        return

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # マーカー間のテキストを置換するための正規表現
    pattern = re.compile(rf"{START_MARKER}.*?{END_MARKER}", re.DOTALL)
    
    # 新しいダッシュボードの内容
    new_dashboard = f"{START_MARKER}\n{generate_dashboard()}\n{END_MARKER}"
    
    if pattern.search(content):
        # すでにマーカーが存在すれば、その間だけを綺麗なダッシュボードに置換
        new_content = pattern.sub(new_dashboard, content)
    else:
        # マーカーがなければ末尾に新しく追記
        new_content = content + f"\n\n{new_dashboard}"

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print("ダッシュボードを更新しました！")

if __name__ == "__main__":
    update_readme()