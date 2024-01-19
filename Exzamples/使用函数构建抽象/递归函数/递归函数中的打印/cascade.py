def cascade(n):
    """逐步展示数字 n 的每一级前缀:
    对于给定的数字，从整个数字开始，逐步减少末位数字，直至剩下最左边的一位数字，然后再依次回到原始数字"""
    if n<10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)

"""将重复的print(n)前置"""
def cascade(n):
    print(n)
    if n >=10:
        cascade(n//10)
        print(n)