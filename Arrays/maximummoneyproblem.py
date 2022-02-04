# https://practice.geeksforgeeks.org/problems/maximum-money2855/1/?company[]=Amazon&company[]=Amazon&page=1&query=company[]Amazonpage1company[]Amazon
import math

def maximizeMoney(N , K):
    if(N == 1):
        return K
    elif(N%2 == 0):
        return int((N/2)*K)
    else:
        return int((math.floor(N/2)+1)*K)

print maximizeMoney(291,566)