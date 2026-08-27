class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        bracketMap = {')': '(', 
                      '}': '{', 
                      ']': '['}
        
        for char in s:
            if char in bracketMap:
                if len(stack) > 0:
                    topVal = stack.pop()
                else:
                    return False
                if topVal != bracketMap[char]:
                    return False
            else:
                stack.append(char)
        
        return len(stack) == 0