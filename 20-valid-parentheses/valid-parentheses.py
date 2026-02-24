class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in pairs:
                top = '#' if not stack else stack.pop()
                if top != pairs[char]:
                    return False
            else:
                stack.append(char)
                
        return len(stack) == 0