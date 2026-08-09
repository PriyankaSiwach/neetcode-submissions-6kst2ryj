class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        newpath= path.split("/")
        for i in newpath:
            if i=="" or i==".":
                continue
            if i=="..":
                if stack: stack.pop()
            else:
                stack.append(i)
        return "/"+ "/".join(stack)
            
