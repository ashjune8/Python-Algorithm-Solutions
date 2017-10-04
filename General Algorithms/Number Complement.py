def findComplement(num):
    stringbin = bin(num)[2:]
    complement = ''

    for i in range(len(stringbin)):
        if stringbin[i] == '0':
            complement += '1'
        else:
            complement += '0'

    return int(complement.format(int),2)


print findComplement(5)

