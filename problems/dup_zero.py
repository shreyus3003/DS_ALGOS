def dup_zero(arr):
    i=0
    while i< len(arr):
        if arr[i] == 0:
            arr.insert(i+1,0)
            arr.pop()
            i = i+2
        else:
            i = i+1

arr = [1,0,2,3,0,4,5,0]
dup_zero(arr)
print(arr)