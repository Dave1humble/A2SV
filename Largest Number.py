class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b):
            ab = str(a) + str(b)
            ba = str(b) + str(a)
            return (ba < ab) - (ab < ba)  
        strs = [str(num) for num in nums]
        strs.sort(key=cmp_to_key(compare))  
        result = ''.join(strs[::-1])  
        return "0" if result == '0'*len(result) else result
