class Solution:
    def rotateString(self, A,B) -> bool:
        return len(A) == len(B) and B in A + A