class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index=0
        j=0
        nums[index]=nums[0]
        index+=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]: 
                j+=1
                if j<2:
                    nums[index]=nums[i] max,min=0,float("inf")
        for cash in prices:
            if cash<min:
                min=cash
            elif cash-min>max:
                max=cash-min
        return max
                    index+=1
            if nums[i]!=nums[i-1]:
                nums[index]=nums[i]
                index+=1
                j=0
        return index