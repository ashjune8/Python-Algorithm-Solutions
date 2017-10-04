

def runLengthEncode(input):

    dict = {}
    uniqueletter = []
    finalstring = ''

    for i in range(len(input)):
        if input[i] in dict:
            dict[input[i]] = dict[input[i]] + 1
        else:
            dict[input[i]] = 1
            uniqueletter.append(input[i])

    for i in uniqueletter:
        count = dict[i]
        finalstring = finalstring + str(count) + i

    return finalstring

print runLengthEncode("GGGGGrrrrrrrrrrrrrrt")


