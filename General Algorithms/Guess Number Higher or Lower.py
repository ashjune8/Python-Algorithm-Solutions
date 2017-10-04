def guessNumber(self, n):
    """
    :type n: int
    :rtype: int
    """
    low = 1
    high = n
    x = (low + high) / 2
    while (guess(x) != 0):
        if guess(x) == -1:
            high = x
            x = (low + high) / 2
        if guess(x) == 1:
            low = x + 1
            x = (low + high) / 2
    return x

