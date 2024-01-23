#在 Python 程序中，更常见的是直接使用列表推导式而不是高阶函数，但这两种序列处理方法都被广泛使用。

"""
列表推导式
[<map expression> for <name> in <sequence expression> if <filter expression>]

为了计算列表推导式,Python 首先执行 <sequence expression>,
它必须返回一个可迭代值。然后将每个元素值按顺序绑定到 <name>,
再执行 <filter expression>,
如果结果为真值，则计算 <map expression>,<map expression> 的结果将被收集到结果列表中。
"""

#完美数是等于其约数之和的正整数。n 的约数指的是小于 n 且可以整除 n 的正整数。
#可以使用列表推导式来列出 n 的所有约数。
def divisor(n):
    return [1] + [x for x in range(2,n) if n % x ==0]

#通过 divisors，我们可以使用另一个列表推导式来计算 1 到 1000 的所有完美数。
#（1 通常也被认为是一个完美数，尽管它不符合我们对约数的定义。）

[n for n in range(1,1000) if sum(divisor(n)==n)]

"""在给定面积的情况下计算具有整数边长的矩形的最小周长。
矩形的面积等于它的高乘以它的宽，因此给定面积和高度，我们可以计算出宽度。"""

def width(area,height):
    assert area % height ==0
    return area // height

#矩形的周长
def perimeter(width,height):
    return (height+width)*2

#最小周长
def min_perimeter(area):
    heights = divisor(area)
    perimeters = [perimeter(width(area,h),h) for h in heights]
    return min(perimeters)

"""高阶函数的表示方式"""

