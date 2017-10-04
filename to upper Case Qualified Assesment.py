def toCapCase(string):

    lst = string.split()
    newlst = []

    for i in range(len(lst)):
        newlst.append(lst[i][0].upper() + lst[i][1:] )


    return " ".join(newlst)

print toCapCase("How can mirrors be real if our eyes aren't real")

