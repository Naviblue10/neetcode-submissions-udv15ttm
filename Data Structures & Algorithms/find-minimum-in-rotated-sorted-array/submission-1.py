class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while(l<=r):
            m=(l+r)//2
            if m==l and m==r:
                return nums[m]
            if nums[m]<nums[r]:
                r=m
            elif nums[m]>nums[r]:
                l=m+1
            