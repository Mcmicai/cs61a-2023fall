def sum_digits(n):
    if n<10:
        return n
    else:
        all_but_last, last = n//10,n%10
        return sum_digits(all_but_last)+last
    

#阶乘函数
    
def factorial(n):
    if n==0:
        return 1
    else:
        return n* factorial(n-1)