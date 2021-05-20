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
nums.insert(1,10)
print("nums", nums)
print("pop", nums.pop())
print("2nd nums",nums)
print("pop with index1", nums.pop(1))
print("3rd nums",nums)
print("remove element 7",nums.remove(2))
print("final nums", nums)

# sortArrayByParityII(nums)