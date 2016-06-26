def rec_sum(n):
    
    if n == 0:
        return 0
    else:
        return n + rec_sum(n-1)
        
print rec_sum(4)

def sum_func(n):
    # Base case
    if len(str(n)) == 1:
        return n
    
    # Recursion
    else:
        return n%10 + sum_func(n/10)


        
print sum_func(12345)