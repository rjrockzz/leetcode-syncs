class Solution:
    def toLowerCase(self, s: str) -> str:
        str_list = list(s)
        for index,i in enumerate(str_list):
            if i.isalpha() and ord(i)<97:
                str_list[index] = chr(ord(i)+32)
        return "".join(str_list)