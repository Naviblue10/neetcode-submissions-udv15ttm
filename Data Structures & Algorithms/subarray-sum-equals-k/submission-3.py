class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        this_dict={
            0:1
        }
        sum=0
        count=0
        for i in nums:
            sum+=i
            if (sum-k) in this_dict:
                count+=this_dict[sum-k]
            if sum in this_dict:
                this_dict[sum]+=1
            else:
                this_dict[sum]=1
        return count
