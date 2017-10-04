import sys
def  secondSmallest(x):

    if len(x) <2:
        return 0
    minimum = sys.maxint
    secondminimum = sys.maxint

    for i in range(len(x)):
        if x[i] < minimum:
            secondminimum = minimum
            minimum = x[i]

        elif x[i] == minimum or x[i] < secondminimum:
            secondminimum = x[i]

    return secondminimum

