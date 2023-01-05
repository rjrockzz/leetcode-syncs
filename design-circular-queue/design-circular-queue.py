class MyCircularQueue:

    def __init__(self, k: int):
		# Allocate memory space 
        self.buffer = [0] * k
        self.limit = k
		
		# We need to track the start index and the number of data stored.
        self.start = 0
        self.cnt = 0

    def enQueue(self, value: int) -> bool:
        if (self.isFull()):
            return False
		
		# Store the value into the last available spot
        self.buffer[(self.start + self.cnt) % self.limit] = value
        self.cnt += 1
        return True
        

    def deQueue(self) -> bool:
        if (self.isEmpty()):
            return False
        
		# Just need to increase the start position, and decrease the number of data stored.
        self.start = (self.start + 1) % self.limit
        self.cnt -= 1
        return True

    def Front(self) -> int:
        if (self.isEmpty()):
            return -1
        return self.buffer[self.start]
        

    def Rear(self) -> int:
        if (self.isEmpty()):
            return -1
        return self.buffer[(self.start + self.cnt - 1) % self.limit]
        

    def isEmpty(self) -> bool:
        return self.cnt == 0
        

    def isFull(self) -> bool:
        return self.cnt == self.limit