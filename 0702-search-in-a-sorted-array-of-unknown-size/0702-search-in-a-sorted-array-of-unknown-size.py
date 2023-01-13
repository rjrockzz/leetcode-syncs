# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        # Since we're unaware of the right most index, which will be an issue.
        # Let's see how we can solve this problem
        #  Let's take two first indexes, 0 and 1, as left and right boundaries. 
        # If the target value is not among these zeroth and the first element, 
        # then it's outside the boundaries, on the right.
        # That means that the left boundary could moved to the right, and the 
        # right boundary should be extended. To keep logarithmic time complexity,
        # let's extend it twice as far: right = right * 2.

        if reader.get(0) == target:
            return 0
        
        # search boundaries
        left, right = 0, 1
        while reader.get(right) < target:
            left = right
            right  <<=1
        # Extend right boundary: right *= 2. To speed up, use right shift instead of multiplication: right <<= 1.
        # binary search
        while left <= right:
            pivot = left + ((right - left) >> 1)
            num = reader.get(pivot)
            
            if num == target:
                return pivot
            if num > target:
                right = pivot - 1
            else:
                left = pivot + 1
        
        # there is no target element
        return -1
