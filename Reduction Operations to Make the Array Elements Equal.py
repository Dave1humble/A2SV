class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        nums.sort()
        for i in range(n-1, 0, -1):
            if nums[i] != nums[i-1]:
                count += (n-i)
            
        return count
