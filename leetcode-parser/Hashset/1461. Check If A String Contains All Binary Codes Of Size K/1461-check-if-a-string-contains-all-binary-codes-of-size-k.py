class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # We need to check if the binary representations of all values up to k are present in the string s.
        # the k is contrained to upto 20, but k is actually the length which can be possible.
        # We need only to check all sub-strings of length k.
        # The number of distinct sub-strings should be exactly 2^k.
        # The naive approach will be to find all the possible strings we can generate from the given k and check it with the given s.

        # BUT we know that the possible number of binary strings we can generate from the given k can be 2k. So let’s check for all possible substrings in s and then we can verify the unique numbers with all possibility numbers ie. 2k.
        unique_sets = set()
        i = 0
        while i<=len(s)-k:
            unique_sets.add(s[i:i+k])
            i+=1
        return len(unique_sets)==2**k
    