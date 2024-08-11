class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        
        closest = float('inf')
        

        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                current_threesum  = num + nums[l] + nums[r]
                
                if abs(current_threesum - target) < abs(closest - target):
                    closest = current_threesum

                if current_threesum == target:
                    return current_threesum
                elif current_threesum < target:
                    l += 1
                else:
                    r -= 1
        return closest
                    
           

        

        
