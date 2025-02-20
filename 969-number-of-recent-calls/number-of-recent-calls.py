class RecentCounter:

    def __init__(self):
        self.queue = []
    
    def ping(self, t: int) -> int:
        if not self.queue:
            self.queue.append(t)
            return 1
        else:
            self.queue.append(t)
            count = 0
            idxToDel = -1
            for idx in range(len(self.queue)-1, -1, -1):
                if self.queue[idx] in range(t-3000, t+1):
                    count+=1
                else:
                    idxToDel = idx
                    break
                    
            if idxToDel >= 0:
                self.queue = self.queue[idxToDel+1:]
            
            return count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)