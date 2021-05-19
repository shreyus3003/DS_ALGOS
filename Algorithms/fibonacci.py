def fibonacci(x):
    arr = [0,1]
    res = 1
    for i in range(2,x+1):
        res = arr[i-2] + arr[i-1]
        arr.append(res)
        # print(arr)
    return arr[x]

# Fibonacci with recursion
def fibonaccir(x,cal):
    arr = []
    cal[0] = cal[0] +1
    if x < 2:
        return x

    res=0
    return fibonaccir(x-1,cal) + fibonaccir(x-2,cal)

# print(res)


# Fibnocci with recursion and caching
cache = {}
cal = [0]
def fibnoccifast(n, cal):
    print(cache)
    if n < 2:
        return n
    if n in cache:
        return cache[n]
    else:
        cal[0] = cal[0] + 1
        cache[n] = fibnoccifast(n-1, cal) + fibnoccifast(n-2, cal)
        return cache[n]



n=10
# for i in range(n+1):
#     print(fibonaccir(i))
# print(fibonacci(8))
print(cache)
print(fibnoccifast(n, cal))
# print(fibonaccir(n,cal))
print(cal)