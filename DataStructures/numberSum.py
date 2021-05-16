
arr = [6,4,3,2,1,7]
sum = 10

# function to find the pair which equals to sum.
# Naive method using 2 loops
# Time complexity is O(n^2)

def pairSum(arr, sum):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] == sum:
                return arr[i], arr[j]
    return 0,0

# Function by using map
# time complexity is O(n)

def pairSum2(arr, sum):
    map ={}
    for i in range(len(arr)):
        if arr[i] in map.values():
            return True
        map[i] = sum - arr[i]
        print(map.values())
    return False

ele1 = pairSum2(arr, sum)
print(ele1)