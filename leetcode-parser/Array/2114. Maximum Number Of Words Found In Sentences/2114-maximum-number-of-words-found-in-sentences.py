class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_so_far = 0
        for i in sentences:
            max_so_far = max(max_so_far, len(i.split(" ")))
        return max_so_far