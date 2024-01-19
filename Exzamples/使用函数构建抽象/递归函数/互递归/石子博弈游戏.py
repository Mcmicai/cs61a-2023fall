"""
桌子上最初有 n 个石子，玩家轮流从桌面上拿走一个或两个石子，
拿走最后一个石子的玩家获胜。
假设 Alice 和 Bob 在玩这个游戏，两个人都使用一个简单的策略：

Alice 总是取走一个石子
如果桌子上有偶数个石子,Bob 就拿走两个石子，否则就拿走一个石子
"""

def play_alice(n):
    if n==0:
        print("Bob wins!")
    else:
        play_bob(n-1)

def play_bob(n):
    if n==0:
        print("Alice wins!")
    elif is_even(n):
        play_alice(n-2)
    else:
        play_alice(n-1)