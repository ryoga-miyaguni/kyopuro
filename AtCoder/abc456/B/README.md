# B - abc456_b

- **URL:** https://atcoder.jp/contests/abc456/tasks/abc456_b
- **難易度:** B

## 問題文
6つの面を持つサイコロが3個あります。

i個目のサイコロのj個目の面にはA_{i,j}が書かれています。

どのサイコロも、各面が出る確率は\frac{1}{6}です。

これらのサイコロを同時に振ったとき、4,5,6の書かれた目が1つずつ出る確率を求めてください。



---

## 解答ステータス
- [x] ✅ 自力AC
- [ ] 📖 解説AC（復習が必要）
- [ ] 🧪 実装のみ参考（ロジックは自力）

## 考察・学んだこと
- 今回書いたコードは正解はしているが、コードがとても読みにくい。sorted を使うことでよりわかりやすく解くことができる

```python
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

count = 0

# 全ての組み合わせを試す
for i in A:
    for j in B:
        for k in C:
            # 3つの目をリストにしてソートするか、集合(set)にして比較する
            if sorted([i, j, k]) == [4, 5, 6]:
                count += 1

print(count / 216)
```

- 昇順 (Ascending): sorted([6, 4, 5]) → [4, 5, 6]
- 降順 (Descending): reverse=True という引数を追加する。sorted([4, 5, 6], reverse=True) → [6, 5, 4]
- 今回は３つが違う数字であるため set を使うこともできる

## 関連アルゴリズム
- 
