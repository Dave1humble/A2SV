class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for chr in s:
            if chr in ['(', '[', '{']:
                stack.append(chr)
            elif chr == ')' and len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            elif chr == ']' and len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            elif chr == '}' and len(stack) != 0 and stack[-1] == '{':
                stack.pop()
            else:
                return False
        return stack == []
