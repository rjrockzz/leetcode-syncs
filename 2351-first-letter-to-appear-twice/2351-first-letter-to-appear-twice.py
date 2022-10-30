class Solution:
    def repeatedCharacter(self, s):
        seen = set()

        for i in s:
            if i not in seen:
                seen.add(i)
            else:
                return i

            