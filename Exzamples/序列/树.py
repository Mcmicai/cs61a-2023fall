def tree(root_label,branches = []):
    for branch in branches:
        assert is_tree(branches)
    return [root_label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree)!=list or len(tree)<1:
        return False
    for branch in branches:
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)


"""树递归"""
def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left,right = fib_tree(n-2)+fib_tree(n-1)
        fib_n = label(left) + label(right)
        return tree(fib_n,[left,right])
    
def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in branches(tree)]
        return sum(branch_counts)
    
"""分割树"""

def partition_tree(n,m):
      """返回将 n 分割成不超过 m 的若干正整数之和的分割树"""
      if n==0:
          return tree(True)
      elif n < 0 or m == 0:
          return tree(False)
      else:
          left = partition_tree(n-m,m)
          right = partition_tree(m.m-1)
          return tree(m,[left,right])
    
"""分割树的所有分割方案打印"""
def print_parts(tree,partition=[]):
    if is_leaf(tree):
        if label(tree):
            print('+'.join(partition))
        else:
            left,right = branches(tree)
            m = str(label(tree))
            print_parts(left,partition+[m])
            print_parts(right,partition)


def right_binarize(tree):
    """根据tree 构造一个右分支的二叉树"""
    if is_leaf(tree):
        return tree
    if len(tree) > 2:
        tree = [tree[0],tree[1:]]
    return [right_binarize(b) for b in tree]