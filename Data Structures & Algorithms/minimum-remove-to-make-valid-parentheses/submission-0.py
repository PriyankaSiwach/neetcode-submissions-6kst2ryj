class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        cnt=0
        for i in s:
            if i=="(":
                stack.append(i)
                cnt+=1
            elif i==")":
                if cnt>0:
                    cnt-=1
                    stack.append(i)
            else:
                stack.append(i)
        filtered=[]
        for i in range(len(stack)-1,-1,-1):
            if stack[i]=="(" and cnt>0:
                cnt-=1
            else:
                filtered.append(stack[i])
        return "".join(filtered[::-1])



            