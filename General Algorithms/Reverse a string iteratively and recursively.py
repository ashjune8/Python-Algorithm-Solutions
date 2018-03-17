def reversestring_iterative(s):
    solution = ''
    for i in range(len(s)-1,-1,-1):
        solution += s[i]

    return solution

def reverse_recursively(s):
    if len(s) == 1:
        return s
    else:
        return reverse_recursively(s[1:]) + s[0]

print reverse_recursively('hello all')





