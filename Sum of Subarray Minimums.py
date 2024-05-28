class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        
        prev = [-1] * n
        next_ = [n] * n
        
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                prev[i] = stack[-1]
            stack.append(i)
        
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                next_[i] = stack[-1]
            stack.append(i)
        
        result = 0
        for i in range(n):
            left = i - prev[i]
            right = next_[i] - i
            result = (result + arr[i] * left * right) % MOD
        
        return result
