import sys
def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    Min = [sys.maxint]*(amount+1)
    Min[0] = 0
    for i in range(1,amount+1):
        for j in range(0,len(coins)):

            if(coins[j] <= i and Min[i-coins[j]] + 1<Min[i]):
                Min[i] = Min[i-coins[j]] + 1
    if Min[amount] == sys.maxint:
        return -1
    return Min[amount]

print coinChange([2],3)