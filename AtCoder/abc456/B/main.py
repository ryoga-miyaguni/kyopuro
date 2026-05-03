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
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))
  C = list(map(int, input().split()))

  count = 0

  for i in A:
    if i == 4:
      for j in B:
        if j == 5:
          for k in C:
            if k == 6:
              count +=1
        elif j == 6:
          for k in C:
            if k == 5:
              count +=1
    elif i == 5:
      for j in B:
        if j == 4:
          for k in C:
            if k == 6:
              count +=1
        elif j == 6:
          for k in C:
            if k == 4:
              count +=1
    elif i == 6:
      for j in B:
        if j == 4:
          for k in C:
            if k == 5:
              count +=1
        elif j == 5:
          for k in C:
            if k == 4:
              count +=1

  print(count / 216)
  pass

if __name__ == '__main__':
  main()