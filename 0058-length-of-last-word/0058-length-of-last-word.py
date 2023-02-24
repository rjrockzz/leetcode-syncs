class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        s_lst = s.split()
        return len(s_lst[-1])