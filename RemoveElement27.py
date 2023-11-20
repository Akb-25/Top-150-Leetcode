class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if val not in nums:
            return len(nums)
        index=0
        for i in range(len(nums)):
            if nums[i]==val:
                pass
            else:
                nums[index]=nums[i]
                index+=1
        return index