import sys

inputline = sys.stdin.readline()
hits = 0
runs = 0
strikes = 0
flag = 0
i =0
while i < (len(inputline))-5:
    if inputline[i] == '(' or inputline[i] == ')' or inputline[i] == ',' or inputline[i] == ' ':
        i += 1
        continue
    if inputline[i] == 'F' and inputline[i+4] == 'F':
        runs = hits +1
        flag = 0
        i = i + 5
    elif inputline[i] == 'F' and inputline[i+4] == 'S':
        strikes += 1
        if strikes == 3:
            print runs
            break
        flag = 0
        i = i+5
    elif inputline[i] == 'C' and inputline[i+3] == 'S':
        hits += 1
        if hits >= 4 and flag == 1:
            runs += 1
            hits -= 1
        flag = 1
        i = i+4

    elif inputline[i] == 'C' and inputline[i+3] == 'F':
        strikes += 1
        if strikes == 3:
            print runs
            break
        flag = 0
        i = i+4

