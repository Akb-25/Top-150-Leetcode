class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1:
            return 1
        visited=set()
        graph={}
        for i in trust:
            if i[0] not in graph:
                graph[i[0]]=[i[1]]
                visited.add(i[1])
            else:
                graph[i[0]].append(i[1])
                visited.add(i[1])
        nodes=set(graph.keys())
        priest=list(visited-nodes)
        if n-len(nodes)>1:
            return -1
        if priest:
            for node in graph:
                if priest[0] not in graph[node]:
                    return -1
            return priest[0]
        return -1