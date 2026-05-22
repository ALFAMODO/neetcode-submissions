class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        # h1, h2 = {}, {}

        # for ch in s:
        #     h1[ch] = h1.get(ch, 0) + 1
        # for ch in t:
        #     h2[ch] = h2.get(ch,0) + 1
        
        # return h1 == h2

        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0)+1

        for ch in t:
            if ch not in count:
                return False
            
            count[ch] -= 1
            if count[ch] == 0:
                del count[ch]
            
        return not count
