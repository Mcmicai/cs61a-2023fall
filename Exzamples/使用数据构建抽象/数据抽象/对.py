#list列表
pair = [10,20]
x,y=pair
print(x)
print(y)


#元素选择运算符的等效函数
from operator import getitem

print(getitem(pair,0))
print(getitem(pair,1))

#双元素列表
"""
def rational(n,d):
    return [n,d]

def numer(x):
    return x[0]

def denom(x):
    return x[1]

half =rational(1,2)
"""

#将有理数简化为最小项
from math import gcd

def rational(n,d):
    g = gcd(n,d)
    return(n//g,d//g)