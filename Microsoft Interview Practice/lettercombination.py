# https://leetcode.com/problems/letter-combinations-of-a-phone-number/solution/

def letterCombinations(digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        lookup = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        
        letter_lists = []
        for ch in digits:
            letter_lists.append(lookup[ch])
            
        while len(letter_lists) > 1:
            l1 = letter_lists.pop()
            l2 = letter_lists.pop()
            combos = []
            for i in l1:
                for j in l2:
                    combos.append(j + i)
            letter_lists.append(combos)
            
        return [] if not letter_lists else letter_lists[0]

print (letterCombinations('232'))