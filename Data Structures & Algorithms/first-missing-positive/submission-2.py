class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        nums=list(set(nums))
        nums.sort()
        j=1
        for i in nums:
            if i>0:
                if i!=j:
                    return j
                j+=1
        return j