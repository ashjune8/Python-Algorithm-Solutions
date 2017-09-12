import sys

def correctoutput(t,p,_type,v):
    if _type == 1:
        status = False
        for i in range(len(t)):
            if p[i] >= v:
                print t[i]
                status = True
                break
            continue
        if status == False:
            print -1
    else:
        maximum = -sys.maxint-1
        indextotaken = 0
        status = False
        if v in t:
            indextotaken = t.index(v)
            status = True
        else:
            for i in range(len(t)):
                if t[i] >= v:
                    indextotaken = i
                    status = True
                    break
                continue
        if status == False:
            print -1
        else:
            for i in range(indextotaken,len(t)):
                maximum = max(maximum,p[i])
            print maximum

inp = []
try:
    while True:
        inp.extend(map(int, raw_input().split()))
except:
    pass
n, q = inp[0], inp[1]
t = inp[2:2 + n]
p = inp[2 + n:2 + 2 * n]
base = 2 + 2 * n
que = []
for i in xrange(q):
    _type, v = (inp[base + 2 * i], inp[base + 2 * i + 1])
    _type, v = [int(_type), int(v)]
    correctoutput(t,p,_type,v)



#if __name__ == "__main__":
 #   n, q = raw_input().strip().split(' ')
  #  n, q = [int(n), int(q)]
   # t = map(int, raw_input().strip().split(' '))
    #p = map(int, raw_input().strip().split(' '))
    #for a0 in xrange(q):
     #   _type, v = raw_input().strip().split(' ')
      #  _type, v = [int(_type), int(v)]
       # correctoutput(t,p,_type,v)
t = [1,2,4,8,10]
p = [5,3,12,1,10]
_type = 2
v = 3
correctoutput(t,p,_type,v)


