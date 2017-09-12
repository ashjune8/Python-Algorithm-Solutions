import sys

def feeOrUpfront(n, k, x, d, p):
    k = float(k)
    x = float(x)
    p = map(float, p)
    d = float(d)
    first_option_sum = long(0)
    for i in range(len(p)):
        first_option_sum += max(k,(((x*p[i]/100))))
    if first_option_sum < d:
        return "fee"
    elif first_option_sum == d:
        return "fee"
    else:
        return "upfront"



n = 3
k = 20
x = 10
d = 60
p = [100,200,300]
print feeOrUpfront(n,k,x,d,p)