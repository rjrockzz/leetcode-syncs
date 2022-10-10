# Check half of the string,
# replace a non 'a' character to 'a'.

# If only one character, return empty string.
# Otherwise repalce the last character to 'b'
class Solution:
    def breakPalindrome(self, S):
        for i in range(len(S) // 2):
            if S[i] != 'a':
                return S[:i] + 'a' + S[i + 1:]
        return S[:-1] + 'b' if S[:-1] else ''