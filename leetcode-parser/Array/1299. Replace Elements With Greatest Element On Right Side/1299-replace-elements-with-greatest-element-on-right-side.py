# A One Pass Solution will go as follows:
# * We traverse the array from the right-most end, and keep a note of
#   the greatest that we've enountered so far.
# It's interesting how running forward causes O(N^2) runtime and backward O(N). Nice solution!
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mod_arr = []
        max_so_far = max(arr[-1], -1)
        mod_arr.append(-1)
        for i in range(len(arr)-2, -1, -1):
                max_so_far = max(max_so_far, arr[i+1])
                mod_arr.append(max_so_far)
        return mod_arr[::-1]
                
                
        