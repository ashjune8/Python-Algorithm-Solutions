import sys

n = int(sys.stdin.readline())
ar = [int(i) for i in sys.stdin.readline().split()]

ar = sorted(ar)

median = n/2

print ar[median]