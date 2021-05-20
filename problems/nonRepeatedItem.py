def nonrepeat(nums):
    hash = {}
    for i in nums:
        hash[i] +=1
    print(hash)

    for i in hash:
        if hash[i] == 1:
            return i


from collections import defaultdict

def singleNumber(nums):
    hash_table = defaultdict(int)
    print(hash_table)
    for i in nums:
        hash_table[i] += 1
    print("2", hash_table)
    for i in hash_table:
        if hash_table[i] == 1:
            return i
nums = [2,2,1]
print(singleNumber(nums))