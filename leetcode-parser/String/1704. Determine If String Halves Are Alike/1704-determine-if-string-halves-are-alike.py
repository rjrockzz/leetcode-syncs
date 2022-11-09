class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        vowel_left = 0
        for index, n in enumerate(s):
            if n in vowels:
                if index<(len(s)//2):
                    vowel_left+=1
                else:
                    vowel_left-=1
        return True if vowel_left==0 else False
                
        