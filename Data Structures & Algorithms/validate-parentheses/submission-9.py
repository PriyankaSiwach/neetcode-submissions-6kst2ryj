class Solution:
    def isValid(self, s: str) -> bool:
        adj={"}": "{", "]":"[", ")":"("}
        stack=[]
        for i in s:
            if i in adj:
                if stack and stack[-1]==adj[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return False if stack else True