class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        for i in range(len(nums2)):
            for j in range(i, len(nums2)):
                if nums2[j] > nums2[i]:
                    hashmap[nums2[i]] = nums2[j]
                    break
                hashmap[nums2[i]] = -1
        for i in range(len(nums1)):
            nums1[i] = hashmap[nums1[i]]
        return nums1
            
            