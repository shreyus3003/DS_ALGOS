def getSum(a,b):
    a_bin = bin(a).replace("0b","00000000")
    b_bin = bin(b).replace("0b","0")
    print(a_bin)
    print(b_bin)
    res = a_bin or b_bin
    print("res", res)
    mem = {}
    res=[]
    for i in range(len(a_bin)):
        mem[i] = int(a_bin[i])
    print(mem)
    j = len(b_bin)-1
    # for j in range(len(b_bin)):
    car = 0
    while j >= 0:
        print(mem[j], b_bin[j])
        if mem[j] == int(b_bin[j]) and int(b_bin[j]) == 1 and car ==1:
            res.append(1)
            car = 1
        elif mem[j] == int(b_bin[j]) and int(b_bin[j]) == 1:
            res.append(0)
            car = 1
        elif mem[j] == int(b_bin[j]) and int(b_bin[j]) ==0:
            if car ==1:
                res.append(1)
                car = 0
            else:
                res.append(0)
        elif car==1:
            res.append(0)
            car = 0
        else:
            res.append(1)


        j -= 1
    print(res)



a=1000
b=4
# print(getSum(a,b))
my_dict={'Name':'Shreyus','Age':30,'magic':False}
print(my_dict)
a = list(my_dict.keys())
print(a[0])