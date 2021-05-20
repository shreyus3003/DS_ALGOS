def maxprofit(prices):
    maxp = 0
    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            prof = prices[j] - prices[i]
            if prof > maxp:
                maxp = prof
    return maxp
def maxprofit2(prices):
    check={}
    min = prices[0]
    for i in range(len(prices)-1):
        if prices[i+1] < min :
            min = prices[i+1]
    print(min)
    maxp = 0
    for j in range(len(prices)):
        prof = prices[j] -min
        if prof > maxp:
            maxp = prof
    return maxp


prices = [2,4,1]
print(maxprofit(prices))