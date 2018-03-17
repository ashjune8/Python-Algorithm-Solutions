def fibonacci_iterative(n):
    lst = []
    lst.append(1)
    lst.append(1)
    for i in range(2,n+1):
        lst.append(lst[i-1] + lst[i-2])

    return lst[n]

def fibonnaci_recursive(n):
    if n < 2:
        return 1
    else:
        return fibonnaci_recursive(n-1) + fibonnaci_recursive(n-2)

print fibonnaci_recursive(5)
print fibonacci_iterative(4)