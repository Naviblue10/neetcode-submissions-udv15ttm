class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        i=0
        max=nums[0]
        flag=False
        temp_flag=True
        prev_flag=False
        while not flag:
            if i>0:
                if nums[i-1]>=max:
                    max=nums[i-1]
                    temp_flag=True
                else:
                    temp_flag=False
                temp_flag=bool(temp_flag and prev_flag)
                prev_flag=temp_flag
            
            
            if i<len(nums)-1 and nums[i]>nums[i+1]:
                nums[i],nums[i+1]=nums[i+1],nums[i]
            
            elif i==len(nums)-1: 
                if temp_flag:
                    flag=True
                i=0
                prev_flag=True
                temp_flag=True    
                max=nums[0]
                continue
            i+=1
        return nums 