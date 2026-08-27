class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l,prev=1,nums[0]
        while l<len(nums):
            if nums[l]==prev:
                nums.pop(l)
            else:
                prev=nums[l]
                l+=1
        return len(nums)
