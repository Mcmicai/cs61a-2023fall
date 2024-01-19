def trace(fn):
    def wrapped(x):
        print('->',fn,'(', x ,')')
        return fn(x)
    return wrapped

@trace
def triple(x):
    return 3*x

print(triple(12))


"""
等价于:triple = trace(triple)
在你的代码中,triple 函数被作为参数传递给了 trace 函数，因此在 trace 函数内部,fn 相当于 triple。
具体来说:

当你使用 @trace 装饰器装饰 triple 函数时，相当于调用了 trace(triple)。
这会使得 trace 函数的参数 fn 成为 triple 函数本身。
因此，在 wrapped 函数内部，当你调用 fn(x) 时，实际上是调用了 triple(x)。
在这个场景中，装饰器 trace 被用来在调用 triple 函数之前打印一些信息（即函数名和传递的参数），然后执行 triple 函数本身，并返回其结果。
"""