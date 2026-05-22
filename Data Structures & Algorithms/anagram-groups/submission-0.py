from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            l[key].append(word)
        return list(l.values())
