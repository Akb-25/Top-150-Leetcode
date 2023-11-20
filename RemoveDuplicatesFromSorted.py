class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        elif len(nums)==0:
            return 0
        index=0
        nums[index]=nums[0]
        index+=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[index]=nums[i]
                index+=1
        return index