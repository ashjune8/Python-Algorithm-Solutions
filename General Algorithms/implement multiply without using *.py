def newmultiply(a,b):
    maximum = max(a,b)
    minimum = min(a,b)
    solution = 0
    for i in range(minimum):
        solution += maximum

    return solution

print newmultiply(10,2)