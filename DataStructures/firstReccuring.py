def firstRecurring(arr):
    dict = {}

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return arr[i]
    return False

def firstRecurring2(arr):
    map={}
    for i in range(len(arr)):
        if arr[i] in map.values():
            return arr[i]
        map[i] = arr[i]
        print(map)

    return False

def checkMap(arr):
    map={}
    chk={}
    for i in range(len(arr)):
        if arr[i] not in map.values():
            map[i] = arr[i]
        if arr[i] not in chk:
            chk[i] = arr[i]
        print("map",map)
        print("chk",chk)

arr = [2,5,5,1,2,3,5,1,2,4]
# res = firstRecurring(arr)
print(checkMap(arr))