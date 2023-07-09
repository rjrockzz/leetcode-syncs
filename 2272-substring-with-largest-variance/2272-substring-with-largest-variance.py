class Solution:
    def largestVariance(self, s: str) -> int:
        res = 0
        freq = Counter()
        char_pos = defaultdict(list)
        for i,c in enumerate(s):
            freq[c] += 1
            char_pos[c].append(i)
        for a in freq.keys():
            for b in freq.keys():
                if a == b:
                    continue
                a_count = b_count = 0
                a_left = len(char_pos[a])
                a_idx = b_idx = 0
                A, B = len(char_pos[a]), len(char_pos[b])
                while a_idx < A or b_idx < B:
                    if a_idx < A and b_idx < B and char_pos[a][a_idx] < char_pos[b][b_idx] or b_idx == B:
                        a_count += 1
                        a_idx += 1
                        a_left -= 1
                    elif b_idx < B:
                        b_count += 1
                        b_idx += 1
                    if b_count < a_count and a_left > 0:
                        a_count = b_count = 0
                    if a_count > 0 < b_count:
                        res = max(res, b_count - a_count)
        return res