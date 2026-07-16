class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        visit= set(deadends)
        def children(lock):
            res=[]
            for i in range(4):
                digit= str((int(lock[i])+1)%10)
                res.append(lock[:i]+digit+lock[i+1:])
                second= str((int(lock[i])-1+10)%10)
                res.append(lock[:i]+second+lock[i+1:])
            return res
        q= deque()
        q.append(["0000", 0])
        while q:
            lock, turn= q.popleft()
            if lock==target:
                return turn
            for child in children(lock):
                if child in visit:
                    continue
                visit.add(child)
                q.append([child, turn+1])
        return -1

