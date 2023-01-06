class Solution:
    def confusingNumber(self, n: int) -> bool:
        hashmap = {0:0, 1:1, 6:9, 8:8, 9:6}
        str_number = list(str(n))
        for index,i in enumerate(str_number):
            if int(i) in hashmap:
                str_number[index] = str(hashmap[int(i)])
            else:
                return False
        return True if int("".join(str_number[::-1]))!=n else False
x = Solution()
print(x.confusingNumber(6))