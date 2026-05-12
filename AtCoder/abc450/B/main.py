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
    N = i_input()

    # 縦 N+1 行、横 N+1 列の「0で埋め尽くされた正方形の表」を作っているというイメージ
    cost = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N):
        line = i_list()

        for k in range(len(line)):
            target_station = i + 1 + k
            cost[i][target_station] = line[k]
    
    for a in range(1, N + 1):
        for b in range(a + 1, N + 1):
            for c in range(b + 1, N + 1):
                if cost[a][b] + cost[b][c] < cost[a][c]:
                    print("Yes")
                    return
                
    print("No")

    pass

if __name__ == '__main__':
    main()
