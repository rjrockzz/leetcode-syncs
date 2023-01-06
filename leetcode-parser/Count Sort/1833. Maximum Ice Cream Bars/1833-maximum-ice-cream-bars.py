from typing import List
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        counter = 0
        costs.sort()
        for i in costs:
            if i<=coins:
                counter+=1
                coins-=i
            else:
                break
        return counter
x = Solution()
print(x.maxIceCream([1,3,2,4,1],7))
