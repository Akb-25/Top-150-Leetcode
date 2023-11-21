class Solution:
    def candy(self, ratings: List[int]) -> int:
        size=len(ratings)
        if size==0:
            return 0
        if size==1:
            return 1
        candies=[1]*size
        for i in range(1,size):
            if ratings[i]>ratings[i-1]:
                candies[i]=candies[i-1]+1
        for i in range(size-2,-1,-1):
            if ratings[i]>ratings[i+1] and candies[i]<=candies[i+1]:
                candies[i]=candies[i+1]+1
        return sum(candies)