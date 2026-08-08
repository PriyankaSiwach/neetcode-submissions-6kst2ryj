class Solution:
    def isValid(self, s: str) -> bool:
        closetoopen= {']':'[', '}': '{', ')': '('}
        stack=[]
        for i in s:
            if i in closetoopen:
                if stack and closetoopen[i]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
            
