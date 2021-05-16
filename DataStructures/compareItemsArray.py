
# Function to check if an array1 item is present in array2 using brute force method
# O(n^2) or O(a*b){since 2 array items are involved)
def commonItemsArray(a1, a2):
    for i in range(len(a1)):
        for j in range(len(a2)):
            if a1[i] == a2[j]:
                return True
    return False

# Function written to reduce the time complexity,
# Creating a map hash table for the first array and comparing the second array elements with the hash table.
# O(n) or O(a+b)
def commonItemsArray2(a1, a2):
    map = {}
    for i in range(len(a1)):
        if a1[i] not in map:
            item = a1[i]
            map[item] = True
    for j in range(len(a2)):
        if a2[j] in map:
            return True
    return False

a1 = ['a', 'b','c',1]
a2 = ['x','y', 'z']

result = commonItemsArray2(a1,a2)
print(result)

