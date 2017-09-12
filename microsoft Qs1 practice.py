import sys
while True:
    inputline = sys.stdin.readline().split()
    if inputline == []:
        print ''
        break
    else:


        currentseparator = ''
        futureseparator = ''
        for i in range(len(inputline[1])):
            if inputline[1][i] == 'm' or inputline[1][i] == 'd' or inputline[1][i] == 'y':
                continue
            else:
                currentseparator = inputline[1][i]
                break

        for i in range(len(inputline[2])):
            if inputline[2][i] == 'm' or inputline[2][i] == 'd' or inputline[2][i] == 'y':
                continue
            else:
                futureseparator = inputline[2][i]
                break
        date = inputline[0].split(currentseparator)
        currentformat = inputline[1].split(currentseparator)
        futureformat = inputline[2].split(futureseparator)

        dictionary = {}

        for i in range(len(currentformat)):
            dictionary[currentformat[i]] = date[i]

        finaloutputlist = []

        for i in range(len(futureformat)):
            finaloutputlist.append(dictionary[futureformat[i]])

        finaloutputstring = finaloutputlist[0] + futureseparator + finaloutputlist[1] + futureseparator + finaloutputlist[2]

        print finaloutputstring