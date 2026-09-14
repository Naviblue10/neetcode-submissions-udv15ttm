class Solution:
    def findMin(self, nums: List[int]) -> int:
        num=set(nums)
        return min(num)