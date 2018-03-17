def number_needed(a, b):
    dictacharinb = {}
    dictbcharina = {}
    commonele = []
    count = 0

    for i in range(len(a)):
        if a[i] in b:
            if a[i] not in dictacharinb:
                dictacharinb[a[i]] = 1
            else:
                dictacharinb[a[i]] +=1
            commonele.append(a[i])

    for i in range(len(b)):
        if b[i] in a:
            if b[i] not in dictbcharina:
                dictbcharina[b[i]] = 1
            else:
                dictbcharina[b[i]] +=1

    for i in range(len(commonele)):
        if dictbcharina[commonele[i]] == dictacharinb[commonele[i]]:
            count += dictacharinb[commonele[i]]
        elif dictbcharina[commonele[i]] > dictacharinb[commonele[i]]:
            count += dictacharinb[commonele[i]]
        else:
            count += dictbcharina[commonele[i]]




    return (len(a) - count) + (len(b)-count)

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
