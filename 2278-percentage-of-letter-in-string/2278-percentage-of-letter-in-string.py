class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        total = len(s)
        total_counts = Counter(s)
        return (total_counts[letter]*100)//total