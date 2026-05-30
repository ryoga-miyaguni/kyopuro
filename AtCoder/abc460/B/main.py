import sys
from math import gcd, ceil, floor, sqrt, pi, factorial, hypot
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
    T = i_input()
    C = i_row_list(T)
    
    for i in range(T):
        x1, y1, r1, x2, y2, r2 = C[i]
        d2 = (x1 - x2) ** 2 + (y1 - y2) ** 2
        if (r1 - r2) ** 2 <= d2 <= (r1 + r2) ** 2:
            print("Yes")
        else:
            print("No")

    pass

if __name__ == '__main__':
    main()
