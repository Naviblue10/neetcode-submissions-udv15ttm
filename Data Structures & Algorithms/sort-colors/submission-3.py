class Solution:
    def sortColors(self, nums: List[int]) -> None:
        colr_count=[nums.count(i) for i in range(3)]
        sorted_nums=[]
        for i in range(len(nums)):
            nums.pop()
        for i in range(3):
            nums.extend([i]*colr_count[i])
        nums=sorted_nums
        return nums
        


        