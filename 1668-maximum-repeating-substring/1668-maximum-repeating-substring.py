class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ans = 1
      # while sequence.find(word * ans) >= 0:
        while word * ans in sequence:           
            ans += 1
        return ans - 1
        