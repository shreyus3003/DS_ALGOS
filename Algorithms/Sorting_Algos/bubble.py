def Sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] < nums[j]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
        print(nums)
    return

def bubbleSort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

    return

def selectSort(nums):
    for i in range(len(nums)):
        min = i
        temp = nums[i]
        for j in range(i+1,len(nums)):
            if nums[j] < nums[min]:
                min = j
        nums[i] = nums[min]
        nums[min] = temp
        print(nums)
    return

nums = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
selectSort(nums)
print(nums)