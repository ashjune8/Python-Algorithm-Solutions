
def findprimenumbers(x):

    lst= []
    lst.append(2)

    count = 1
    number = 3
    prime = True
    while count < x :
        for i in range(0,len(lst)):
            if number%lst[i] == 0:
                prime = False
                break
        if prime == False:
            number += 1
            prime = True
        else:
            lst.append(number)
            count += 1
            number += 1
            prime = True

    return lst

print findprimenumbers(10)

