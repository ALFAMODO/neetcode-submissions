class Solution:

    def encode(self, strs: List[str]) -> str:
        l=[]
        for i in strs:
            l.append(str(len(i)))
            l.append("#")
            l.append(i)
        return ''.join(l)
        

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        n=len(s)
        while i<n:
            j=i
            while s[j] != "#":
                j = j+1

            length = int(s[i:j])
            start = j + 1
            end = start + length
            word = s[start:end]
            res.append(word)

            i = end
        return res        
