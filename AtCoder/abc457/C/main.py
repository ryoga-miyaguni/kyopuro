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
    N, K = i_map()
    A_info = i_row_list(N)  
    C = i_list()

    # 各ブロックを順に判定
    for i in range(N):
        # A_info[i][0] が Li、それ以降が実際の数列 Ai
        L_i = A_info[i][0]
        A_i = A_info[i][1:]
        C_i = C[i]
        
        # このブロック全体の長さ
        total_len = L_i * C_i
        
        if K <= total_len:
            # K番目がこのブロック内にある場合
            # (K-1) % L_i で、数列 Ai 内のどのインデックス（0-indexed）か特定
            idx = (K - 1) % L_i
            print(A_i[idx])
            return
        else:
            # このブロックに K番目がなければ、その分を K から引いて次へ
            K -= total_len
    
    pass

if __name__ == '__main__':
    main()
