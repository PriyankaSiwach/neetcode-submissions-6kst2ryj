class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack=[]
        for i in range(len(ops)):
            if ops[i]=="+":
                a=stack[-1]
                b=stack[-2]
                stack.append(a+b)
            elif ops[i]=="D":
                a=stack[-1]
                stack.append(2*a)
            elif ops[i]=="C":
                stack.pop()
            else:
                stack.append(int(ops[i]))
        return sum(stack)
