def convertinttobinarylongmethod(n):

    lst = []

    while n != 0:
        lst.append(n%2)
        n= n/2
    return lst[::-1]

print convertinttobinarylongmethod(4)

print bin(4)[2:]