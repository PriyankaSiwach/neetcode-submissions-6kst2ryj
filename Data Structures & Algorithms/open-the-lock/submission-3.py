class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        visit= set(deadends)
        def dfs(lock):
            res=[]
            for i in range(4):
                digit= str((int(lock[i])+1)%10)
                res.append(lock[:i]+digit+lock[i+1:])
                sec= str((int(lock[i])-1+10)%10)
                res.append(lock[:i]+sec+lock[i+1:])
            return res
        q=deque()
        q.append(["0000",0])
        while q:
            lock,turn= q.popleft()
            if lock==target:
                return turn
            for i in dfs(lock):
                if i in visit :
                    continue
                visit.add(i)
                q.append([i,turn+1])
        return -1
        
