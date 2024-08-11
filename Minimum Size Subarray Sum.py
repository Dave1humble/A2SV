class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        res = len(nums) + 1  
        curr = 0
        
        while right < len(nums):
            curr += nums[right]
            while curr >= target:
                res = min(res, right - left + 1) 
                curr -= nums[left]  
                left += 1
            
            right += 1  
        return res if res <= len(nums) else 0  











        
        
