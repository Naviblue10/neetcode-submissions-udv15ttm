class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l,r=0,1
        while r<len(nums):
            if nums[l]==nums[r]:
                nums.pop(r)
            else:
                l+=1
                r+=1
            print(nums)
            print(l,r)
        return len(nums)
