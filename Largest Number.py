class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = list(map(str, nums))
        def compare(a: str, b: str) -> int:
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0
        nums_str.sort(key=cmp_to_key(compare))
        largest_num = ''.join(nums_str)
        return largest_num if largest_num[0] != '0' else '0'
