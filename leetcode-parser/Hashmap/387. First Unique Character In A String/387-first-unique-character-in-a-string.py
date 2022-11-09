class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = Counter(s)
        counter = 0
        for i in s:
            if hashmap[i]==1:
                return counter
            else:
                counter+=1
        return -1