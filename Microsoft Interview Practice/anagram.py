# https://leetcode.com/explore/interview/card/microsoft/30/array-and-strings/200/

def groupAnagrams(strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mapping = {}
        finalList = []

        for i in range(len(strs)):
            tempList = sorted(strs[i])
            tempString = ''.join(tempList)
            if  tempString in mapping:
                mapping[tempString].append(strs[i])
            else:
                mapping[tempString] = []
                mapping[tempString].append(strs[i])

        for i in mapping:
            finalList.append(mapping[i])

        return finalList

print (groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

