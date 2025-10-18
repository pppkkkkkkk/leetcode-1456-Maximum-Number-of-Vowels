class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        firstIdx = 0
        maxVowCnt = 0
        curVowCnt = 0
        curNumCnt = 0 
        volDict = {"a":True, "e":True, "i":True, "o":True, "u":True}

        for char in s:
            if k > curNumCnt:
                curNumCnt+=1
            else:
                if s[firstIdx] in volDict:
                    curVowCnt -= 1
                firstIdx += 1
            if char in volDict:
                curVowCnt += 1
            maxVowCnt = max(maxVowCnt, curVowCnt)
        
        return maxVowCnt