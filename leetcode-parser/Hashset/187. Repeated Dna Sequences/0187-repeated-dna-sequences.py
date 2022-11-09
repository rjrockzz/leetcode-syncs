class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        result_set = set()
        final_set = set()
        i = 0
        while i<=len(s)-10:
            if s[i:i+10] in result_set:
                final_set.add(s[i:i+10])
            else:
                result_set.add(s[i:i+10])
            i+=1
        return list(final_set)