def sortArrayByParityII(nums):
    t = 0
    for i in range(len(nums) + 1):
        if nums[i] % 2 == 0:
            nums[t] = nums[i]
            t = t + 2
    t = 1
    for i in range(len(nums) + 1):
        if nums[i] % 2 != 0:
            nums[t] = nums[i]
            t = t + 2

nums = [4,2,5,7]
sortArrayByParityII(nums)