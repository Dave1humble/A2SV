class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i + 1]:
                nums[i] = (nums[i]) * 2 
                nums[i + 1] = 0
            continue    
        left = 0
        right = n - 1
        while left < right:
            if nums[left] == 0:
                nums.pop(left)
                nums.append(0)
                right-=1
            else:
                left+=1
        return nums
