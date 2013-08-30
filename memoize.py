def fib_slow(n):
    return n if n<2 else fib_slow(n-1) + fib_slow(n-2)


def fib_memoir(n):
    cache = {}
    if n in cache.keys():
        return cache.get(n) 
    else:
        if n < 2:
            cache[n] = n
        else:
            cache[n] =fib_memoir(n-1) + fib_memoir(n-2)
    return cache.get(n)


class memoir(object):
    def __init__(self,fn):
        self.fn = fn
        self.cache = {}
    def __call__(self, *args): 
        if args not in self.cache: 
            self.cache[args] = self.fn(*args) 
        return self.cache[args]


#memo: fib = memo(fib)
def memo(f):
    cache = {}
    def _f(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return _f

@memo
def fib(n):
    return n if n<2 else fib(n-1) + fib(n-2)  

@memoir
def f(x,y): # 2 arguments, must unpack before
    return x+y

