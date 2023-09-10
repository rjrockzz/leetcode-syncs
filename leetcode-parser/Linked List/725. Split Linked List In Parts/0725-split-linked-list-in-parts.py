class Solution(object):
    def splitListToParts(self, root, k):
        cur = root
        for N in range(1001):
            if not cur: break
            cur = cur.next
        width, remainder = divmod(N, k)

        ans = []
        cur = root
        for i in range(k):
            head = cur
            for j in range(width + (i < remainder) - 1):
                if cur: cur = cur.next
            if cur:
                cur.next, cur = None, cur.next
            ans.append(head)
        return ans