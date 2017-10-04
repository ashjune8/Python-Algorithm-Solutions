import sys

n = int(sys.stdin.readline())
arr = [int(i) for i in raw_input().strip().split()]
#arr = [int(i) for i in "-20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854 -520 -470".split()]
#n = 12
arr = sorted(arr)

dict = {}
minimum = sys.maxint
for i in range(n-1):
    minimum = min(minimum, abs(arr[i] - arr[i+1]))
    if abs(arr[i] - arr[i+1]) == minimum:
        if minimum not in dict:
            dict[minimum] = str(arr[i]) + " " + str(arr[i+1])
        else:
            dict[minimum] = dict[minimum]+ " " + str(arr[i]) + " " + str(arr[i+1])

print dict[minimum]


