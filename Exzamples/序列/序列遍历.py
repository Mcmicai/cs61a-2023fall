"""统计一个值在序列中出现了多少次"""

def count(s,value): 
    total = 0
    for elem in s:
        if elem == value:
            total=total+1
    return total