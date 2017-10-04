import math
import sys
def  bestAverageGrade(scores):
    if scores == []:
        return 0
    Max = float('-inf')
    dictionary = {}
    for i in range(len(scores)):
        if scores[i][1] == "" or scores[i][1] == "":
            return 0
        if scores[i][0] not in dictionary:
            dictionary[scores[i][0]] = []
            dictionary[scores[i][0]].append(float(scores[i][1]))

        else:
            dictionary[scores[i][0]].append(float(scores[i][1]))
    temp = 0
    for i in dictionary:
        temp = float(sum(dictionary[i]))/float(len(dictionary[i]))
        Max = max(Max,temp)

    return int(math.floor(Max))

print bestAverageGrade([["s","87"],["e","100"],["j","64"],["e","22"]])