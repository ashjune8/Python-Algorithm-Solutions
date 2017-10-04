def solution(N):
    binaryoriginalnumber = bin(N)[2:]
    nextnumber = N
    found = False

    while found == False:
        nextnumber = nextnumber + 1
        binarynextnumber = bin(nextnumber)[2:]
        found = checksparse(binarynextnumber)

    return nextnumber


def checksparse(binarynextnumber):

    for i in range(len(binarynextnumber)-1):
        if binarynextnumber[i] == '1' and binarynextnumber[i+1]=='1':
            return False

    return True



print solution(100)
print bin(128)[2:]
