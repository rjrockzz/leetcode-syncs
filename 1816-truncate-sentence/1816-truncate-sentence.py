class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        str_lst = s.split(" ")
        return " ".join(str_lst[:k])