class Solution:
    def replaceDigits(self, s: str) -> str:
        str_list = list(s)
        for index, n in enumerate(s):
            if n.isnumeric():
                str_list[index]=chr(ord(str_list[index-1])+int(n))
        return "".join(str_list)