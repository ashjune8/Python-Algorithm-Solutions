# https://practice.geeksforgeeks.org/problems/print-first-letter-of-every-word-in-the-string3632/1/?company[]=Amazon&company[]=Amazon&page=1&query=company[]Amazonpage1company[]Amazon

def firstAlphabet(S):

    arr = S.split(" ")
    result=""
    for i in range(len(arr)):
        result = result + arr[i][0]

    return result

print firstAlphabet("geeks for geeks")
