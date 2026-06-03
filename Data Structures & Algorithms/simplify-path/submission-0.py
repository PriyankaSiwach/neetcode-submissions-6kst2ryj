class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        newpath= path.split("/")
        for c in newpath:
            if c=="" or c==".":
                continue
            elif c =="..":
                if stack: stack.pop()
            else:
                stack.append(c)
        return "/" + "/".join(stack)

        
        