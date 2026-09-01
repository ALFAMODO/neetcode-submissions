class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        current = ""

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            
            elif ch == "[":
                stack.append((current, num))
                current=""
                num = 0
            
            elif ch == "]":
                prev, number = stack.pop()
                current = prev + current * number

            else:
                current += ch

        return current 
            
        