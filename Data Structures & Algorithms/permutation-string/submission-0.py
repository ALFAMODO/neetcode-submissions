from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False

        count_s1 = Counter(s1)
        window_count = Counter()
        left = 0

        for right in range(len_s2):
            window_count[s2[right]] += 1
            if right - left + 1 > len_s1:
                left_char = s2[left]
                window_count[left_char] -= 1
                if window_count[left_char] == 0:
                    del window_count[left_char]
                
                left+=1
            if window_count == count_s1:
                return True
        return False
        