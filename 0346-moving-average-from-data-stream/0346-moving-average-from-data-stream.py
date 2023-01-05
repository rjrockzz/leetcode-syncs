from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.counter = 0
        self.sum_so_far = 0
        self.size = size
        self.deque = deque([])

    def next(self, val: int) -> float:
        if len(self.deque)==self.size:
            self.deque.popleft()
        self.deque.append(val)
        return sum(self.deque)/len(self.deque)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)