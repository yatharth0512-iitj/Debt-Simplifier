import heapq

class BinaryHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self, value):
        heapq.heappush(self.heap, (-value[0], value[1]))
    
    def size(self):
        return len(self.heap)
    
    def empty(self):
        return self.size() == 0
    
    def extractMax(self):
        if self.empty():
            return None
        neg_val, index = heapq.heappop(self.heap)
        return (-neg_val, index)