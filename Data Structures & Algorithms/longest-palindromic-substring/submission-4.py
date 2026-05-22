class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        maxLen = 0

        def findMax(l, r):
            while l>=0 and r<len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l+1, r-1

        for i in range(len(s)):
            l , r = findMax(i, i)
            if r-l+1 > maxLen:
                res =s[l: r+1]
                maxLen = r-l+1
            
            l , r = findMax(i, i+1)
            if r-l+1 > maxLen:
                res =s[l: r+1]
                maxLen = r-l+1
        
        return res
            
            
