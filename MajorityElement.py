class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occurences={}
        for i in range(len(nums)):
            if nums[i] not in occurences:
                occurences[nums[i]]=1
            else:
                occurences[nums[i]]+=1
        keyMax=0
        keyVal=0
        for key,val in occurences.items():
            if val>keyVal:
                keyVal=val
                keyMax=key
        return keyMax


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate=0
        count=0
        for i in range(nums):
            if count==0:
                maxVal=nums[i]
            if candidate==nums[i]:
                count+=1
            elif candidate!=nums[i]:
                count-=1
        return candidate
