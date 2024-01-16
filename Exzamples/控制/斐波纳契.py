def fib(n):
    pred,curr =0,1
    k=2
    while k<n:
        pred,curr = curr,pred+curr
        k+=1
    return curr

def print_fib(n):
    pred,curr = 0,1
    k=2
    print(pred)
    while k<=n:
        print(curr)
        pred,curr = curr,pred+curr
        k+=1
