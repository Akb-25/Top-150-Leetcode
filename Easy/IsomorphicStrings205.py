class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sMap={}
        tMap={}
        for i,j in zip(s,t):
            if i not in sMap:
                sMap[i]=j
            else:
                if sMap[i]!=j:
                    return False
            if j not in tMap:
                tMap[j]=i
            else:
                if tMap[j]!=i:
                    return False
        return True