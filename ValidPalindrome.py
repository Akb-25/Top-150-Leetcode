class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s= ""
        for i in s:
            i = i.lower()
            if i.isalnum():
                new_s += i
        last=len(new_s)-1
        for i in range(last // 2 + 1):
            if new_s[i] == new_s[last]:
                last-=1
            else:
                return False
        return True
block=Solution()
output=block.isPalindrome("race a car")
print(output)
