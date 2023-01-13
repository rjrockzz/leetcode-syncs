from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if i[0]<=target and i[len(matrix[0])-1]>=target:
                # Binary Search
                left, right = 0, len(matrix[0])-1
                while left<right:
                    mid = (left + right)//2
                    if i[mid]==target:
                        return True
                    elif i[mid]> target:
                        right = mid
                    else:
                        left = mid+1
                return True if i[left]==target else False
print(Solution().searchMatrix([[1]],1))