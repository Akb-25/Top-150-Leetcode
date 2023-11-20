class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index=0
        occurences={}
        for i in range(len(nums)):
            if nums[i] not in occurences:
                occurences[nums[i]]=1
                nums[index]=nums[i]
            else:
                if occurences[nums[i]]>=2:
                    continue
                occurences[nums[i]]+=1
                nums[index]=nums[i]
            index+=1
        return index