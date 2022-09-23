class Solution:
    def interpret(self, command: str) -> str:
        ans = str_builder = ""
        for i in command:
            str_builder+=i
            if str_builder=="G":
                ans+="G"
                str_builder=""
            if str_builder=="()":
                ans+="o"
                str_builder=""
            if str_builder == "(al)":
                ans+="al"
                str_builder=""
        return ans