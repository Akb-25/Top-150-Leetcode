class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source==destination:
            return True
        visited=set()
        graph={}
        def find(current,destination):
            if current in visited:
                return False
            visited.add(current)
            connections=graph[current]
            for i in connections:
                if i == destination or find(i,destination):
                    return True
            return False
        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = [edge[1]]
            else:
                graph[edge[0]].append(edge[1])
            if edge[1] not in graph:
                graph[edge[1]] = [edge[0]]
            else:
                graph[edge[1]].append(edge[0])
        return find(source,destination)