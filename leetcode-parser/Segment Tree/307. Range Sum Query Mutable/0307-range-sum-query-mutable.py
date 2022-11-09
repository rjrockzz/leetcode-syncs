'''
Segment Tree logic here ->
* Minimum of Range
* Sum of Range
* Maximum of Range
'''
class NumArray:
    # So the logic here is actually similar to the segment trees, but the difference comes 
    # to be in the range sum, instead of finding the minimum element in the array.
    def __init__(self, nums: List[int]):
        self.data = [0 for _ in nums] + nums
        self.n = len(nums)
        
        for idx in range(self.n-1, 0, -1):
            # if n = 5, this will go 4->3->2->1 ie. will update the 0s we initialized above.
            self.data[idx] = self.data[2*idx] + self.data[2*idx + 1]
            
    def update(self, i: int, val: int) -> None:
        idx = i + self.n
        self.data[idx] = val
        while idx > 1:
            idx //= 2
            self.data[idx] = self.data[2*idx] + self.data[2*idx + 1]
        

    def sumRange(self, i: int, j: int) -> int:
        #sum [i,j] = sum [i, j)
        left = i + self.n
        right = j + self.n +1
        sum_range = 0
        while left < right:
            if left%2:
                sum_range += self.data[left]
                left +=1
            if right %2:
                right -= 1
                sum_range += self.data[right]
            left //= 2
            right //= 2
        
        return sum_range