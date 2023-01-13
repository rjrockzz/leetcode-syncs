class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters)
        while left<right:
            mid = (left+right)//2
            if ord(target)<ord(letters[mid]):
                right = mid
            else:
                left = mid+1
        return letters[left%len(letters)]