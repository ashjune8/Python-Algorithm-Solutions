import sys

rotationcount = int(sys.stdin.readline().split()[1])
originalarray = sys.stdin.readline().split()
result = ""

def singleleftrotation(arr):

    temp = arr.pop(0)
    arr.append(temp)
    return arr

for i in range(rotationcount):
    originalarray = singleleftrotation(originalarray)


sys.stdout.write(str.join(" ",originalarray))


