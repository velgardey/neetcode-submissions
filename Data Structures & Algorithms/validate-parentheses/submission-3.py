class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenMap = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        for char in s:
            if char in parenMap:
                if stack and stack[-1] == parenMap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        
        return True if not stack else False