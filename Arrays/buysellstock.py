# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

def maxProfit(prices):

    result = None
    leftPointer = 0
    rightPointer = 1

    if len(prices) == 1:
        return 0
    while leftPointer != len(prices)-2:
        if result == None:
            result = prices[rightPointer] - prices[leftPointer]
            rightPointer += 1
        else:
            result = max(result, prices[rightPointer] - prices[leftPointer])
            rightPointer += 1
        if rightPointer == len(prices) - 1:
            result = max(result, prices[rightPointer] - prices[leftPointer])
            leftPointer += 1
            rightPointer = leftPointer + 1
        
    
    result = max(result, prices[rightPointer] - prices[leftPointer])

    
    if result < 0:
        return 0

    return result

print (maxProfit([7,1,5,3,6,4]))