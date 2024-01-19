"""求正整数 n 的分割数，最大部分为 m,
即 n 可以分割为不大于 m 的正整数的和，并且按递增顺序排列。
例如，使用 4 作为最大数对 6 进行分割的方式有 9 种。
"""

def count_partitions(n,m):
    if n==0:
        return 1
    elif n<0:
        return 0
    elif m==0:
        return 0
    else:
        return count_partitions(n-m,m)+count_partitions(n,m-1)