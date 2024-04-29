class Solution:
    def lengthOfLongestSubstring(self, s):
        right = 0
        left = 0
        max_length = 0
        chr_str = set()
        while right < len(s):
            if s[right] not in chr_str:
                chr_str.add(s[right])
                max_length = max(max_length, right - left + 1)
                right += 1  
            else:
                chr_str.remove(s[left])
                left += 1  
        return max_length
