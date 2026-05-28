class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold=len(nums)/3
        res=[]
        uniq_vals=list(set(nums))
        counts=[nums.count(i) for i in uniq_vals]
        for i,a in enumerate(counts):
            if a>threshold:
                res.append(uniq_vals[i])
        return res
            
