class Solution:
    def freqAlphabets(self, s: str) -> str:
        # traversing from the right once we encounter
        # a #, we take the next two values
        # and find the value from the hashmap.
        hashmap = {}
        str_builder = ""
        for i in range(97,123):
            hashmap[i-96]=chr(i)
        size = len(s)-1
        while size>-1:
            if s[size]=="#":
                str_builder+=hashmap[int(s[size-2]+s[size-1])]
                size-=3
            else:
                str_builder+=hashmap[int(s[size])]
                size-=1      
        return str_builder[::-1]
x = Solution()
print(x.freqAlphabets(s = "10#11#12"))
