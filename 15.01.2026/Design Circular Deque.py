class MyCircularDeque(object):

    def __init__(self, k):
        self.queue=deque(maxlen=k)
        self.size=k


        

    def insertFront(self, value):
        if len(self.queue)<self.size:
            self.queue.appendleft(value)
            return True
        else:
            return False
        
        

    def insertLast(self, value):
        if len(self.queue)<self.size:
            self.queue.append(value)
            return True
        else:
            return False
        

    def deleteFront(self):
        if self.queue:
            self.queue.popleft()
            return True
        else:
            return False
                

    def deleteLast(self):
        if self.queue:
            self.queue.pop()
            return True
        else:
            return False        

    def getFront(self):
        if self.queue:
            return self.queue[0]
        else:
            return -1
                

    def getRear(self):
        if self.queue:
            return self.queue[-1]
        else:
            return -1
        

    def isEmpty(self):
        return len(self.queue)==0
        

    def isFull(self):
        return len(self.queue)==self.size
        
