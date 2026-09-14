class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        t=target
        while(l<=r):
            m=(l+r)//2
            if t==nums[m]:
                return m
            elif nums[l]<=nums[m]:
                if nums[l]<=t and t<nums[m]:
                    r=m-1
                else:
                    l=m+1
            elif nums[m]<=nums[r]:
                if nums[m]<t and t<=nums[r]:
                    l=m+1
                else:
                    r=m-1
        return -1
            