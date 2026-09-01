class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i:[] for i in range(n)}

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        q = deque([(0,-1)])

        while q:
            node, parent = q.popleft()

            if node in visited:
                return False
            visited.add(node)

            for nei in graph[node]:
                
                if nei == parent:
                    continue
                
                q.append((nei, node))
            
        return len(visited) == n
