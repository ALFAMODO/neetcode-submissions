from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t:
            return ""

        freq, window = Counter(t), {}
        left = 0
        res = [float("inf"), None, None]
        have, need = 0, len(freq)

        for right, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1

            if ch in freq and window[ch] == freq[ch]:
                have+=1

            while have == need:
                if (right-left+1) < res[0]:
                    res = [right - left +1, left, right]
                
                window[s[left]] -=1
                if s[left] in freq and window[s[left]] < freq[s[left]]:
                    have-=1
                
                left +=1

        l, r = res[1], res[2]
        return s[l:r+1] if res[0] != float("inf") else ""
       



            
        