class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        arr = [k for k,v in Counter(arr).items() if v==1]
        if len(arr)<k:
            return ""
        return [k for k,v in Counter(arr).items() if v==1][k-1]