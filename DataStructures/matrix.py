# a = [['2','1','8'],['0','3','2'],['5','4','8']]
def matrixrep(a):
    sum = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                sum += a[i]
    return sum

def matrixrep2(a):
    map={}
    map2={}
    sum = 0
    for i in range(len(a)):
        if a[i] in map and a[i] not in map2:
            map2[a[i]] = a[i]
        map[a[i]] = a[i]
        print(map)
        print(map2)
    for i in map2:
        sum += map2[i]
    return sum


a = [2,1,8,0,3,2,5,4,8,8,8,9]
print(matrixrep2(a))