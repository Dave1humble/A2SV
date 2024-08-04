class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2  = Counter(nums2)
        res = []
        for num in c1:
            if num in c2:
                min_count = min(c1[num], c2[num])
                for _ in range(min_count):
                    res.append(num)
        return res
    

        
