class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(current:str, openCount:int, closeCount:int):
            if len(current) == 2 * n:
                res.append(current)
                return

            if openCount < n:
                backtrack(current + "(", openCount+1, closeCount)

            if closeCount < openCount:
                backtrack(current + ")", openCount, closeCount+1)

        backtrack("", 0, 0)
        return res

            
       