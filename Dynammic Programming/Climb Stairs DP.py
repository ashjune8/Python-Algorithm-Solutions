
def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 0:
        return 0
    Sol = [0]*(n+1)
    Sol[0] = 0
    Sol[1] = 1
    if n== 1:
        return 1
    Sol[2] = 2

    for i in range(3,n+1):
        Sol[i] = Sol[i-1] + Sol[i-2]

    return Sol[n]

print climbStairs(4)

