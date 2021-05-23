def removeDuplicates(nums):
    i=0
    for j in range(len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    print(nums,i)


nums = [0,0,1,1,1,2,2,3,3,4]
removeDuplicates(nums)