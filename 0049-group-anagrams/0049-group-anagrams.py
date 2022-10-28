class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for i in strs:
            word = "".join(sorted(i))
            hashmap[word].append(i)
        return [*hashmap.values()]