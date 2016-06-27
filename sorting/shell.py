def shell_sort(nums):
    
    h = 1
    n = len(nums)
    while h > 0:
            for i in range(h, n):
                c = nums[i]
                j = i
                while j >= h and c < nums[j - h]:
                    nums[j] = nums[j - h]
                    j = j - h
                    nums[j] = c
            h = int(h / 2.2)
    return nums
    
arr = [1, 3, 2, 7, 5, 4, 9, 7]

print shell_sort(arr)