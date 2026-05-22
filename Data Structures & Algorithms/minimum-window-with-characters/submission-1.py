class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "":
            return ""
        resLen = float('infinity')
        res = [-1, -1]

        countT= {}
        window= {}

        for i in t:
            countT[i] = 1 + countT.get(i, 0)

        have = 0
        need = len(countT)
        l = 0
        for r in range(len(s)):
            c = s[r]  # c = s[0] = "O"
            window[c] = 1 + window.get(c, 0) #window[O] = 1
            print(0, c)

            if c in countT and window[c] == countT[c]:
                have+=1
                print(1, have)
            
            while have==need:
                if r-l+1 < resLen:
                    res = [l, r]
                    resLen = r-l+1
                    print(2, r-l+1, resLen)

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1
            
        l, r = res
        return s[l: r+1] if resLen != float('infinity') else ""


            

        
        

'''
s = "OUZODYXAZV", t = "XYZ"

have = 2
need = 3

have == need
res = l, r 
resLen = min(reslen, r-l+1) -> min(infinity, 2) -> 4

l+=1

countT
{
X: 1
Y: 1
Z: 1
}

window
{
O: 2 -> 1
U: 1 -> 0
Z: 1 -> 0
D: 1 -> 0
Y: 1 -> 0
X: 1
A: 1
V: 1
}

if window[ch] is in countT
have -= 1

return res, resLen

res -> l, r
s[l:r] -> YXAZ
'''