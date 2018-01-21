import sys

def solve(grades):
    # Complete this function
    result = [0]*len(grades)

    for i in range(len(grades)):
        if grades[i] < 38:
            result[i] = grades[i]
        elif ((grades[i]/5)+1)*5 - grades[i] < 3:
            result[i] = ((grades[i]/5)+1)*5
        else:
            result[i] = grades[i]

    return result


n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
print "\n".join(map(str, result))
