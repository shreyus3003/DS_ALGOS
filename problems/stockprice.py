def maxprofit(prices):
    maxp = 0
    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            prof = prices[j] - prices[i]
            if prof > maxp:
                maxp = prof
    return maxp

prices = [[7,1,5,3,6,4]]
print(maxprofit(prices))