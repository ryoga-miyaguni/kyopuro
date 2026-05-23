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
    S = s_list()
    ans = ""

    for i in range(N):
        if S[i][0] == "a" or S[i][0] == "b" or S[i][0] == "c":
            ans += "2"
        elif S[i][0] == "d" or S[i][0] == "e" or S[i][0] == "f":
            ans += "3"
        elif S[i][0] == "g" or S[i][0] == "h" or S[i][0] == "i":
            ans += "4"
        elif S[i][0] == "j" or S[i][0] == "k" or S[i][0] == "l":
            ans += "5"
        elif S[i][0] == "m" or S[i][0] == "n" or S[i][0] == "o":
            ans += "6"
        elif S[i][0] == "p" or S[i][0] == "q" or S[i][0] == "r" or S[i][0] == "s":
            ans += "7"
        elif S[i][0] == "t" or S[i][0] == "u" or S[i][0] == "v":
            ans += "8"
        elif S[i][0] == "w" or S[i][0] == "x" or S[i][0] == "y" or S[i][0] == "z":
            ans += "9"

    print(ans)          
    pass

if __name__ == '__main__':
    main()
