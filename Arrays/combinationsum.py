# https://leetcode.com/problems/combination-sum/

def combinationSum(candidates, target):
        candidates=sorted(candidates) ## Sorting
        combination,n=[],len(candidates)
        def findTargetSum(currSum,index,path):
            if currSum==target:
                combination.append(path)
                return
            for i in range(index,n):
                newSum=candidates[i]+currSum
                if newSum<=target: 
                    findTargetSum(newSum,i,[candidates[i]]+path)
            
        findTargetSum(0,0,[])
        return combination

print (combinationSum([2,3,6,7],7))