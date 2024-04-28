class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s = set(nums2)
        nums1.sort()
        for x in nums1:
            if x in s:
                return x
        return -1
