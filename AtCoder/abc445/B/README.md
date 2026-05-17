# B - abc445_b

- **URL:** https://atcoder.jp/contests/abc445/tasks/abc445_b
- **難易度:** B

## 問題文
英小文字からなるN個の奇数長の文字列S_1,S_2,\dots,S_Nが与えられます。

S_1,S_2,\dots,S_Nのうち最も長いものの長さをmとします。


以下の条件を満たす文字列T_1,T_2,\dots,T_Nを求めてください。

条件：T_iはある非負整数kについてk個の.、S_i、k個の.をこの順に結合してできる、長さmの文字列である。



---

## 解答ステータス
- [x] ✅ 自力AC
- [ ] 📖 解説AC（復習が必要）
- [ ] 🧪 実装のみ参考（ロジックは自力）

## 考察・学んだこと
- 以下の解法でも正解になる
```python
def main():
    N = i_input()
    S = s_row(N) # 前回修正した正しい入力関数

    # 各文字列の長さを集めた中から max を取る（直感的で分かりやすい書き方）
    max_s = max(len(i) for i in S)

    for i in S:
        # i を全体の長さ max_s になるように中央寄せし、隙間を "." で埋める
        print(i.center(max_s, "."))
        
    pass
```
## 関連アルゴリズム
- 
