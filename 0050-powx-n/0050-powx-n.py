class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            # our recursive base cases
            if x == 0:
                return 0
            if n == 0:
                return 1
            # // is the integer division, so we divide the problem
            res = helper(x * x, n // 2)
            # Now we check if the n was odd, then we explicilty multiply an x 
            # to the above computation and return the result
            return x * res if n % 2 else res

        res = helper(x, abs(n))
        # we then finally deal with the negative exponents.
        return res if n >= 0 else 1 / res