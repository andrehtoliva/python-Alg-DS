def insertion_sort(arr):
    
    for i in range(1, len(arr)):
        currentValue = arr[i]
        position = i
        
        while position > 0 and arr[position - 1] > currentValue:
            arr[position] = arr[position - 1]
            position = position - 1
            
        arr[position] = currentValue
        
    return arr
        
arr = [1, 3, 2, 7, 5, 4, 9, 7]
print insertion_sort(arr)