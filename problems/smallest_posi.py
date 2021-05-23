def smalpos(arr):
    for i in range(len(arr)):
        if i not in arr:
            print(i)



arr = [1,3,6,4,1,2]
print(smalpos(arr))