class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k < 0: return self.decrypt(code[::-1], -k)[::-1]
        n = len(code)
        prefix = code * 2
        for i in range(1, 2 * n):
            prefix[i] += prefix[i - 1]
        for i in range(n):
            code[i] = prefix[i + k] - prefix[i]
        return code