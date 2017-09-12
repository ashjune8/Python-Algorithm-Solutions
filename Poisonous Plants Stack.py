import sys

def poisonousPlants(p):
    # Complete this function
    elementtadd = [p[0]]
    days = 0
    condition = True
    while condition:
        for i in range(1,len(p)):
            if p[i] < p[i-1]:
                elementtadd.append(p[i])
        if elementtoremove:
            x = 0
            for i in range(len(elementtoremove)):
                p.pop(i -x)
                x += 1
            elementtoremove = []
            days += 1
        else:
            break
    return days

#if __name__ == "__main__":
    #n = int(raw_input().strip())
    #p = map(int, raw_input().strip().split(' '))
    #result = poisonousPlants(p)
    #print result
print poisonousPlants([3,1,10,7,3,5,6,6])