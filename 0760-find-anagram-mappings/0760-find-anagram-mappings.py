class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        hashmap = {}
        for index, num in enumerate(nums2):
            if num in hashmap:
                hashmap[num].append(index)
            else:
                hashmap[num] = [index]
        for i in nums1:
            result.append(hashmap[i].pop())
        return result