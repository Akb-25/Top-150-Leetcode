class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0]in edges[1]:
            similar=edges[0][0]
        else:
            similar=edges[0][1]
        for edge in edges:
            if similar in edge:
                continue
            else:
                return -1
        return similar