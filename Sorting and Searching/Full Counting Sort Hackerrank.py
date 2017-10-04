import sys

number = int(sys.stdin.readline());

dict = {}
arr = []
input = []

for i in range(number):
    input= sys.stdin.readline().split()
    arr.append(int(input[0]))
    if int(input[0]) not in dict:
        dict[int(input[0])] = []
        dict[int(input[0])].append(input[1])
    else:
        dict[int(input[0])].append(input[1])

for i in range(number/2):
    j = 0
    while j < len(dict[arr[i]]):
        if dict[arr[i]][j] == "-":
            j+=1;
        else :
            dict[arr[i]][j] = "-"
            break

for i in range(number):
    if i in dict:
        j = 0
        while j < len(dict[i]):
            print dict[i][j],

            j+=1;






