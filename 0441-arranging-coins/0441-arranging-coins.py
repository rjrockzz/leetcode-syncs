class Solution:
    def arrangeCoins(self, n: int) -> int:
        x = 1
        while n>=0:
            if n>=x:
                n-=x
                x+=1
            else:
                break
        return x-1
        