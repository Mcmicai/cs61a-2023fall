#用两个函数来实现“对”以及一个二元列表

def pair(x,y):
    """Return a function that represents a pair."""
    def get(index):
        if index ==0:
            return x
        elif index == 1:
            return y
    return get

def select(p,i):
    return p(i)

p = pair(20,14)

select(p,0)
# 20

select(p,1)
# 14