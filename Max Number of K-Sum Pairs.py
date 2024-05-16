class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums_dict = Counter(nums)
        seen = set()
        operations = 0
        for num in nums:
            if num not in seen and nums_dict[k-num] in nums_dict:
                if num == k-num:
                    operations = nums_dict[num]//2
                else:
                    operations+=1
                seen.add(num)
                seen.add(k-num)
            
        return operations
