def hammingDistance(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """

    # binx = []
    # biny = []

    binx = list(bin(x))[2:]
    biny = list(bin(y))[2:]
    # while x != 1:
    # binx.append(x%2)
    # x = x/2

    # if x == 1:
    #    binx.append(1)
    # binx = binx[::-1]

    # while y != 1:
    #    biny.append(y%2)
    #     y = y/2

    # if y == 1:
    #    biny.append(1)
    # biny = biny[::-1]

    maxx = max(len(binx), len(biny))
    minn = min(len(binx), len(biny))

    diff = maxx - minn

    if len(binx) == maxx:
        for i in range(diff):
            biny.insert(0, '0')
    else:
        for i in range(diff):
            binx.insert(0, '0')
    hamm = 0

    for i in range(maxx):
        if binx[i] != biny[i]:
            hamm += 1

    return hamm

print hammingDistance(1,4)