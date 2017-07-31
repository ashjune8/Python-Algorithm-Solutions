def calcEquation(equations, values, queries):
    """
    :type equations: List[List[str]]
    :type values: List[float]
    :type queries: List[List[str]]
    :rtype: List[float]
    """

    dictofdict = {}
    result = []

    for i in range(len(equations)):
        if equations[i][0] not in dictofdict.keys():
            dictofdict[equations[i][0]] = {}
        dictofdict[equations[i][0]][equations[i][1]] = values[i]

        if equations[i][1] not in dictofdict.keys():
            dictofdict[equations[i][1]] = {}
        dictofdict[equations[i][1]][equations[i][0]] = 1/values[i]



    def findpath(dictofdict,start,end):

        if (start not in dictofdict.keys()) or (end not in dictofdict.keys()):
            return -1.0
        if start == end:
            return 1.0

        visited = []

        def findresult(visited,dictofdict,start,end):

            if start not in visited:
                visited.append(start)
            if end in dictofdict[start].keys():
                return dictofdict[start][end]
            else:
                if list((set(dictofdict[start].keys())-set(visited))) == []:
                    return -1
                for i in (list((set(dictofdict[start].keys())-set(visited)))):
                    temp = findresult(visited,dictofdict,start,i)*findresult(visited,dictofdict,i,end)
                    if temp<0:
                        continue
                    else:
                        return temp
                return -1

        return findresult(visited,dictofdict,start,end)



    for i in range(len(queries)):
        result.append(findpath(dictofdict,queries[i][0],queries[i][1]))
    return result

print calcEquation([["x1","x2"],["x2","x3"],["x1","x4"],["x2","x5"]],
[3.0,0.5,3.4,5.6],
[["x3","x4"],["x4","x3"],["x6","x6"],["x0","x0"]])

