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
    N, Q = i_map()
    q = i_row_list(Q)

    ans = [0] * N

    for i in range(Q):
        if q[i][0] == 1:
            ans[q[i][1] - 1] += 1
            if all(x >= 1 for x in ans):
                ans = [l - 1 for l in ans]
        elif q[i][0] == 2:
            count = 0
            for k in range(N):
                if ans[k] >= q[i][1]:
                    count += 1
            print(count)
    pass

if __name__ == '__main__':
    main()
