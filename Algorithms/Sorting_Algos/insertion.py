def insertionSort(nums):
    for i in range(len(nums)):
        pos = i
        cur_val = nums[i]
        for j in range(1,len(nums)):
            if cur_val > nums[j]:
                cur_val = nums[j]
                nums[pos] = nums[j]





nums = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
insertionSort(nums)
print(nums)