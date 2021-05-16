def fibonacci(x):
    arr = [0,1]
    res = 1
    for i in range(2,x+1):
        res = arr[i-2] + arr[i-1]
        arr.append(res)
        # print(arr)
    return arr[x]

def fibonaccir(x):
    arr = []
    if x < 2:
        return x

    res=0
    return fibonaccir(x-1) + fibonaccir(x-2)

# print(res)
n=8
for i in range(n+1):
    print(fibonaccir(i))
# print(fibonacci(8))