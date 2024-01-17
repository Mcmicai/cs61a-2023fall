def imporve(update,close, guess = 1):
    while not close(guess):
        guess = update(guess)
    return guess

def sqrt(a):
    def sqrt_update(x):
        return average(x,a/x)
    def sqrt_close(x):
        return approx_eq(x * x,a)
    return improve (sqrt_update, sqrt_close)