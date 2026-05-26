class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        for i in range(len(nums)):
            prdct=1
            for j in range(len(nums)):
                if j==i:
                    continue
                prdct*=nums[j]
            output.append(prdct)
        return output
        