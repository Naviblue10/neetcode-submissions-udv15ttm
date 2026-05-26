class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        set_nums=list(set(nums))
        max_count=1
        max_num=set_nums[0]
        for i in set_nums:
            if nums.count(i)>max_count:
                max_count=nums.count(i)
                max_num=i
        return max_num


        