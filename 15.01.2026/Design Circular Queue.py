class MyCircularQueue(object):
    def __init__(self, k):
        self.queue = [0] * k
        self.idx = [0, -1]
        self.maxLength = k
        

    def enQueue(self, value):
        currLength = self.idx[1] - self.idx[0] + 1

        if currLength < self.maxLength:
            self.idx[1] = self.idx[1] + 1
            self.queue[self.idx[1] % self.maxLength] = value
            return True
        else:
            return False
        
    def deQueue(self):
        if self.idx[1] < self.idx[0]:
            return False
        else:
            self.idx[0] = self.idx[0] + 1
            return True
    
    def Front(self):
        if self.idx[1] < self.idx[0]:
            return -1
        else:
            return self.queue[self.idx[0] % self.maxLength]
        
    def Rear(self):
        if self.idx[1] < self.idx[0]:
            return -1
        else:
            return self.queue[self.idx[1] % self.maxLength]
        

    def isEmpty(self):
        currLength = self.idx[1] - self.idx[0] + 1

        if currLength == 0:
            return True
        return False

    def isFull(self):
        currLength = self.idx[1] - self.idx[0] + 1

        if currLength == self.maxLength:
            return True
        return False
        
