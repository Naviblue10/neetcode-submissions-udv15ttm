class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        sorted_with_indices=sorted(enumerate(nums), key=lambda x:x[1])
        sorted_list=[item[1] for item in sorted_with_indices]
        indices=[item[0] for item in sorted_with_indices]
        i=0
        while i<len(nums)-1:
            curr_ele=sorted_list[i]
            curr_ind=indices[i]
            next_ele=sorted_list[i+1]
            next_ind=indices[i+1]
            if curr_ele == next_ele:
                if next_ind-curr_ind<=k:
                    return True
            i+=1
        return False

        