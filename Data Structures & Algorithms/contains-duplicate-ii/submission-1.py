class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i=0
        while i<len(nums)-1:
            if nums[i] in nums[i+1:]:
                pos=nums[i+1:].index(nums[i])
                if pos+1<=k:
                    return True
            i+=1
        return False