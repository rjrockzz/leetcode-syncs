from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        counter = 0
        dups = []
        hashmap_string = Counter(s)
        hashmap_values = [*hashmap_string.values()]
        print(hashmap_values)
        hashmap = Counter([*hashmap_string.values()])
        print(hashmap)
        for i in hashmap:
            if hashmap[i]==2:
                dups.append(i)
            if hashmap[i]>2:
                dups+=[i]*(hashmap[i]-1)
        print(dups)
        for n,i in enumerate(dups):
            i_init = i
            while 1:
                i-=1
                counter+=1
                if i==0:
                    break
                if i in hashmap_values:
                    continue
                else:
                    hashmap_values.remove(i_init)
                    hashmap_values.append(i)
                    break
        return counter
