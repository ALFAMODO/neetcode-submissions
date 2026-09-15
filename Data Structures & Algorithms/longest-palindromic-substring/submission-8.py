class Solution:
    def longestPalindrome(self, s: str) -> str:

        length = 0
        index = 0
        for i in range(0, len(s)):
            l, r = i, i
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l+1) > length:
                    index = l
                    length = r-l+1
                l-=1
                r+=1

        
            l, r = i, i + 1
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l+1) > length:
                    index = l
                    length = r-l+1
                l-=1
                r+=1

        return s[index: index+length]