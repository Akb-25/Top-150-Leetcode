def removeElement(nums:list[int],val:int)->int:
        size=len(nums)
        times=0
        i=0
        while i<size:
            if nums[i]==val:
                times+=1
                i+=1
        return size-times
nums=[3,2,3,2]
val=3
print(removeElement(nums,val))