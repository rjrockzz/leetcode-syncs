class Solution:
    def minSwaps(self, s: str) -> int:
        #exactly half are opening and half are closing
        if s=="":
            return 0
        # we'll be keeping a track of all the extra closing brackets 
        extraClose,maxClose = 0, 0
        for i in s:
            if i=="]":
                extraClose+=1
            else:
                extraClose-=1
            maxClose = max(maxClose, extraClose)
        return (maxClose+1)//2