class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        size=len(nums)
        if k>size:
            k=k%size
        nums[:]=nums[size-k:]+nums[:size-k]