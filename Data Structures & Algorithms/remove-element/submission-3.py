class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        not_val=0
        i=0
        while(i<len(nums)):
            if nums[i]==val:
                nums.remove(val)
                i-=1
            else:
                not_val+=1
            i+=1
        return not_val