class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next,self.prev= None,None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.mapp={}
        self.left, self.right= Node(0,0), Node(0,0)
        self.left.next, self.right.prev= self.right, self.left
    
    def insert(self,val):
        prev,next= self.right.prev, self.right
        prev.next= next.prev= val
        val.next, val.prev=next, prev

    def remove(self,val):
        prev,next= val.prev,val.next
        prev.next,next.prev= next, prev

    def get(self, key: int) -> int:
        if key in self.mapp:
            self.remove(self.mapp[key])
            self.insert(self.mapp[key])
            return self.mapp[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mapp:
            self.remove(self.mapp[key])
            self.mapp[key]=value
        self.mapp[key]= Node(key,value)
        self.insert(self.mapp[key])
        if len(self.mapp)> self.cap:
            lru= self.left.next
            self.remove(lru)
            del self.mapp[lru.key]


