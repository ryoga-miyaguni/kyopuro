import sys

def solve():
    # 入力を高速に読み込む
    s = sys.stdin.readline().strip()
    if not s:
        return
    
    n = len(s)
    MOD = 998244353
    
    total_count = 0
    current_segment_length = 1
    
    # 文字列を走査してセグメントの長さを特定する
    for i in range(n - 1):
        if s[i] != s[i+1]:
            # 隣り合う文字が異なるなら、現在のセグメントを伸ばす
            current_segment_length += 1
        else:
            # 同じ文字が隣り合ったらセグメント終了。
            # そのセグメント内での部分文字列の組み合わせ数を加算
            count = (current_segment_length * (current_segment_length + 1)) // 2
            total_count = (total_count + count) % MOD
            # 新しいセグメントを長さ1から開始
            current_segment_length = 1
            
    # 最後のセグメント分を加算
    count = (current_segment_length * (current_segment_length + 1)) // 2
    total_count = (total_count + count) % MOD
    
    print(total_count)

if __name__ == '__main__':
    solve()