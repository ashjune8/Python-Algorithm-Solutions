def reverseWords(s):
    newlist = s.split()

    reversestring = ""

    for i in range(len(newlist)):
        if i == len(newlist)-1:
            reversestring += newlist[i][::-1]
        else:
            reversestring += newlist[i][::-1] + ' '

    return reversestring

print reverseWords("Let's take LeetCode contest")