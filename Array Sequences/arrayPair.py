def pair_sum(array, result):
    
    if len(array) < 2:
        return "Error"
    
    # Sets for tracking
    seen = set()
    output = set()
    
    for num in array:
        target = result - num
        if target not in seen:
            seen.add(num)
        else:
            output.add( ((min(num, target)), max(num, target)) )
            
    return len(output)
            
print pair_sum([1,3,2,2], 4)