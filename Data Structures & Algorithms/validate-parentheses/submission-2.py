class Solution:
    def isValid(self, s: str) -> bool:
        ClosetoOpen= {'}':'{', ']':'[', ')': '(' }
        stack=[]
        for c in s:
            if c in ClosetoOpen:
                if stack and ClosetoOpen[c]== stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
        