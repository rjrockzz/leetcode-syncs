class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        '''
        Each person is labeled with a Unique ID from 0 to n-1
        if if groupSizes[1] = 3, then person 1 must be in a group of size 3.
        '''
        # Rememeber that the array is 0 indexed
        result = []
        hashmap = defaultdict(list)
        for index, n in enumerate(groupSizes):
            if len(hashmap[n])==n:
                result.append(hashmap[n])
                hashmap[n]=[index]
            else:
                hashmap[n].append(index)
        return [*hashmap.values()]+result
        