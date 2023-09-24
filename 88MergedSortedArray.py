# def merge(nums1:list[int],m,nums2:list[int],n)->None:
#     lastm=m-1
#     lastn=n-1
#     while lastm>=0:
#         if nums1[lastm]>nums2[lastn]:
#             nums[lastm+lastn]=nums1[lastm]
#             lastm-=1
#         elif nums1[lastm]<nums2[lastn]:
#             nums1[lastm],nums2[lastn]=nums2[lastn],nums1[lastm]
#     while lastn>=0:
#         nums1[lastm+lastn]=nums2[lastn]
#         lastn-=1
#         return result
# m=[1,2,3,4,0,0,0,0]
# n=[3,4,4,5]
# print(merge(m,len(m),n,len(n)))
def merge(nums1:list[int],m:int,nums2:list[int],n:int):
    last=m+n-1
    m=m-1
    n=n-1
    while n>=0:
        if m>=0 and nums1[m]>nums2[n]:
            nums1[last]=nums1[m]
            m-=1
        else:
            nums1[last]=nums2[n]
            n-=1
        last-=1
    return nums1
arr1=[1,2,3,4,0,0,0,0]
size1=len(arr1)
arr2=[2,3,4,9]
size2=len(arr2)
print(size1)
print(size2)
print(merge(arr1,size1-size2,arr2,size2))