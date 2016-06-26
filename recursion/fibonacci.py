def fib_rec(n):
    
    if (n == 0) or (n == 1):
        return n
    else:
        return fib_rec(n-1) + fib_rec(n-2)
        
def fib_iter(n):
    
    x = 0
    y = 1
    for i in xrange(n):
        z = x + y
        x = y
        y = z 
        
    return x
        
        
print fib_iter(10)
print fib_rec(10)