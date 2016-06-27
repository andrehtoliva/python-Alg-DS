def bubble_sort(arr):
    
    for n in range(len(arr)-1, 0, -1):
        for k in range(n):
            
            if arr[k] > arr[k+1]:
                temp = arr[k]
                arr[k] = arr[k + 1]
                arr[k + 1] = temp
                
    return arr
                
arr = [1, 3, 2, 7, 5, 4, 9, 7]

print bubble_sort(arr)