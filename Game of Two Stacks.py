import sys

def maxscoretwostacks(a,b,x, maxsum, score):

    if a == [] and b== []:
        return score
    elif a == []:
        if maxsum + b[0] > x:
            return score
        else:
            maxsum += b[0]
            b.pop(0)
            score += 1
            return maxscoretwostacks(a,b,x,maxsum,score)
    elif b == []:
        if maxsum + a[0] > x:
            return score
        else:
            maxsum += a[0]
            a.pop(0)
            score += 1
            return maxscoretwostacks(a,b,x,maxsum,score)
    elif a[0] < b[0]:
        if maxsum + a[0] > x:
            return score
        else:
            maxsum += a[0]
            a.pop(0)
            score += 1
            return maxscoretwostacks(a,b,x,maxsum,score)
    elif a[0] > b[0]:
        if maxsum + b[0] > x:
            return score
        else:
            maxsum += b[0]
            b.pop(0)
            score += 1
            return maxscoretwostacks(a,b,x,maxsum,score)
    elif a[0] == b[0]:
        if maxsum + b[0] > x:
            return score
        else:

            return max(maxscoretwostacks(a[1:],b,x,maxsum + a[0],score+1),maxscoretwostacks(a,b[1:],x,maxsum+b[0],score+1))

#g = int(raw_input().strip())
#for a0 in xrange(g):
    #n,m,x = raw_input().strip().split(' ')
    #n,m,x = [int(n),int(m),int(x)]
    #a = map(int, raw_input().strip().split(' '))
    #b = map(int, raw_input().strip().split(' '))
    # your code goes here

    #maxsum = 0
    #score = 0
    #print max(maxscoretwostacks(a,b,x,maxsum,score),maxscoretwostacks([],b,x,maxsum,score),maxscoretwostacks(a,[],x,maxsum,score))

maxsum = 0
score = 0
print max(maxscoretwostacks([4,5,3],[5,2,1],10,maxsum,score),maxscoretwostacks([],[5,2,1],10,maxsum,score),maxscoretwostacks([4,5,3],[],10,maxsum,score))

