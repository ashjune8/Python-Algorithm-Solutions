# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

class Tree(object):
     def __init__(self, x):
         self.x = x
         self.l = None
         self.r = None

def traverse(T, ans, maxValue):
    if(T == None):
        return ans

    if(T.x >= maxValue):
        ans += 1
        maxValue = max(T.x, maxValue)
    
    ans = traverse(T.l,ans,maxValue)

    ans = traverse(T.r, ans,maxValue)

    return ans


def solution(T):
    # write your code in Python 3.6
    global ans
    global maxValue
    ans = 0
    # Cant remeber syntax on how to define maxVlaue as soomething like -sys.max-1 so taking a very low negative number
    maxValue = -100000000 

    return traverse(T,ans,maxValue)

a = Tree(1)
b = Tree(2)
c = Tree(3)
d = Tree(0)
e = Tree(5)
a.l = b
b.l = c
b.r = e
a.r = d

print solution(a)

    




