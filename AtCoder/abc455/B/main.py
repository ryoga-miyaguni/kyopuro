import sys
from math import gcd, ceil, floor, sqrt, pi, factorial
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left, bisect_right
from functools import reduce

# 入力高速化
input = sys.stdin.readline

def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input().rstrip() # 改行文字削除
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)

# 再帰上限の設定（DFS用）
sys.setrecursionlimit(10 ** 6)

# 定数
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    # 1. 入力を受け取る
    # H, W は 1 行に 2 つなので i_map() で展開
    H, W = i_map()
    
    # グリッド（文字列の行）が H 個続くので s_row(H) を使う
    # これで S[i][j] の形で各マスにアクセスできます
    S = s_row(H)

    count = 0

    # 2. 長方形の範囲 (h1, h2, w1, w2) を全探索
    # range(H) は 0 から H-1 までなので、h1, h2 などの添字としてそのまま使えます
    for h1 in range(H):
        for h2 in range(h1, H):
            for w1 in range(W):
                for w2 in range(w1, W):
                    
                    # 3. 選んだ長方形が点対称か判定
                    is_ok = True
                    for i in range(h1, h2 + 1):
                        for j in range(w1, w2 + 1):
                            # 点対称の相手の座標を計算
                            # 0始まりのインデックスでも、問題文の式がそのまま使えます
                            ni = h1 + h2 - i
                            nj = w1 + w2 - j
                            
                            # 色が違えば即座に失敗
                            if S[i][j] != S[ni][nj]:
                                is_ok = False
                                break
                        if not is_ok:
                            break
                    
                    # すべてのマスが一致していればカウント
                    if is_ok:
                        count += 1

    # 4. 結果を出力
    print(count)

if __name__ == '__main__':
    main()