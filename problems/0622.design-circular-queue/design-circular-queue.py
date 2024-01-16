class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        
        self.queue = [None for i in range(k)]
        self.front = self.rear = -1
        

    def enQueue(self, value: int) -> bool:
        if ((self.rear + 1) % self.k == self.front):
            return False
        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.k
            self.queue[self.rear] = value
        return True
        

    def deQueue(self) -> bool:
        if (self.front == -1): return False
        if (self.front == self.rear):
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.k
        return True
        
    def Front(self) -> int:
        if self.front == -1 and self.rear == -1:
            return -1
        return self.queue[self.front]
        

    def Rear(self) -> int:
        if self.front == -1 and self.rear == -1:
            return -1
        return self.queue[self.rear]
        

    def isEmpty(self) -> bool:
        return self.rear == -1
        

    def isFull(self) -> bool:
        return not self.isEmpty() and (self.rear + 1) % self.k == self.front
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()