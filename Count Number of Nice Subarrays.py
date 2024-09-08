class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        odd_count = 0
        left = 0
        subarray_kcount = 0
        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odd_count += 1
            while odd_count > k:
                if nums[left] % 2 == 1:
                    odd_count -= 1
                left += 1
            if odd_count == k:
                temp = left

                while temp < right and nums[temp] % 2 == 0:
                    temp += 1
                subarray_kcount = temp - left + 1
                count += subarray_kcount
        return count
         
        
         
        
