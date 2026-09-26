class Solution:
    def calculate(self, s: str) -> int:
        num=0
        sign="+"
        stack=[]
        for i,c in enumerate(s):
            if c.isdigit():
                num=num*10+int(c)
            if c in "+-*/" or i==len(s)-1:
                if sign=="+":
                    stack.append(num)
                elif sign=="-":
                    stack.append(-num)
                elif sign=="*":
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                sign=c
                num=0
        return sum(stack)


            



