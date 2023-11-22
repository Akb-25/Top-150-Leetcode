class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[1]*n
        suffix=[1]*n
        prefix_product=1
        for i in range(n):
            prefix[i]=prefix_product
            prefix_product*=nums[i]
        suffix_product=1
        for i in range(n-1,-1,-1):
            suffix[i]=suffix_product
            suffix_product*=nums[i]
        result=[prefix[i]*suffix[i] for i in range(n)]
        return result