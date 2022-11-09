# Incredible idea of using iterator! My god, I love this idea!!!! Using iterator we can cut t after finding a character!!!! The beauty is that iterator is only used once in Python. After using iterator, you cannot use it anymore, wow!!! very deep understanding of Python
class Solution:
    def isSubsequence(self, s, t):
        remainder_of_t = iter(t)
        for letter in s:
            if letter not in remainder_of_t:
                return False
        return True

        