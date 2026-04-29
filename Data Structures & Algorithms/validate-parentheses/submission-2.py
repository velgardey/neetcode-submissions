class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        parMap = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        for char in s:
            
            if char in parMap:
                if stk and stk[-1] == parMap[char]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(char)
            
        return True if not stk else False