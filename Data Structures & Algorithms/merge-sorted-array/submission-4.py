class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums1)-m):
            nums1.pop(-1)
        for j in range(len(nums2)-n):
            nums2.pop(-1)
        nums1.extend(nums2)
        nums1.sort()
        