class Solution:     # The problem reduces to whether there is a 
                    # zero in any position other than the last  
                    # position n[-1], and if so, whether there 
                    # is a reachable cell beyond each such zero.  

    def canJump(self, n: list[int]) -> bool:
        
        if 0 not in n[:-1] or len(n) == 1: return True

        pt = n.index(0)            

        for i in range(len(n)):

            if i <= pt and  i + n[i] > pt: pt = i + n[i]

            if i == pt and not n[i]: return False
            if pt >= len(n)-1      : return True

        return True