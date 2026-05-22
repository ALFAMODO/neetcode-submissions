class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        res = set()

        trie = {}
        for word in words:
            node = trie
            for d in word:
                node = node.setdefault(d, {})
            node['#'] = True

        def dfs(r,c,node,path):
            if r<0 or c<0 or r>=rows or c>=cols or board[r][c] not in node:
                return
            
            ch = board[r][c]
            node = node[ch]
            path+=ch

            if "#" in node:
                res.add(path)

            board[r][c] = "*"
            dfs(r+1, c, node, path)
            dfs(r-1, c, node, path)
            dfs(r, c+1, node, path)
            dfs(r, c-1, node, path)

            board[r][c] = ch
        
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,trie, "")
        return list(res)