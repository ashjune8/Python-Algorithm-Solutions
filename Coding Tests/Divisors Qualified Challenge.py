def divisors(integer):
    finalset = set()

    for i in range(2,integer):
        if integer%i == 0:
            finalset.add(i)

    return sorted(list(finalset))

print divisors(12)