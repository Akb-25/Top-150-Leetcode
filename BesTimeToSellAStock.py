class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min=float("inf")
        minKey=-1
        maxKey=-1
        max=0
        for key,val in prices:
            if val<min and key>minKey:
                min=val
                minKey=key
            if val>max and key>maxKey and key>minKey:
                max=val
                maxKey=key
        return max-min