import sys

dictionary = {}
for i in range(5):
    inputline = sys.stdin.readline().strip()
    if inputline in dictionary:
        dictionary[inputline] += 1
    else:
        dictionary[inputline] = 1

maxstring = ''
maxoutput = 0
for i in dictionary:
    if dictionary[i] > maxoutput:
        maxstring = i
        maxoutput = dictionary[i]

print maxstring
print maxoutput

