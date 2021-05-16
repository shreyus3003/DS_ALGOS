def fact(x):
    if x <=0:
        return 1
    return x*fact(x-1)

def fact1(x):
    if x <=0:
        return 1
    res = 1
    for i in range(x+1):
        if i!=0:
            res = res * i
    return res





print(fact(1))