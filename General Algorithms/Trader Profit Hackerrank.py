import sys

def traderProfit(k, n, A):
    # Complete this function
    profit_list = []
    i = 0
    minimum = 0
    maximum = 0
    while k > 0:
        if i < len(A)-1 and A[i] < A





if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        k = int(raw_input().strip())
        n = int(raw_input().strip())
        arr = map(int, raw_input().strip().split(' '))
        result = traderProfit(k, n, arr)
        print result