class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left = set() # (middle, outer), at most 26^2 palindromes
        # The left tells us about all the unique characters on the left of our mid pointer
        res = set()
        # The result will contain the final sets
        right = Counter(s)
        # As we keep moving to the right, we decrease and decrease the counter, that's why it's better to use a hashmap.
        
        for middle_character in range(len(s)): # everytime we get to a character we're looking for the middle character, and once we get the middle character we're no longer looking for that in the right pointer hence why we delete it from the hashmap.
            right[s[middle_character]]-=1
            if right[s[middle_character]]==0:
                right.pop(s[middle_character])
            for j in range(26):
                c = chr(ord("a")+j)
                if c in left and c in right: # we check if the same characters are present in both the left and the right hashsets, If so, then we can add it to our result hashset.
                    res.add((s[middle_character], c))
            left.add(s[middle_character])
        return len(res)
            
            