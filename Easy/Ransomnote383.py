class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts={}
        for i in magazine:
            if i not in counts:
                counts[i]=1
            else:
                counts[i]+=1
        for i in ransomNote:
            if i not in counts:
                return False
            elif i in counts:
                if counts[i]==0:
                    return False
                counts[i]-=1 
        return True