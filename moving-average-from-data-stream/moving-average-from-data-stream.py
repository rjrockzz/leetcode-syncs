from collections import deque
class MovingAverage:
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.length = 0
        self.max = size
        self.sum = 0
        self.queue = deque()

    def next(self, val: int) -> float:
        if self.length < self.max:
            self.length +=1
            self.queue.append(val)
            self.sum += val
        else:
            self.sum -= self.queue.popleft()
            self.queue.append(val)
            self.sum += val
        return self.sum/self.length


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)