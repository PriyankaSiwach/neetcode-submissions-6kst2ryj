class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        adj={'}':'{', ')':'(', ']':'['}
        for c in s:
            if c in adj:
                if stack and stack[-1]==adj[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False