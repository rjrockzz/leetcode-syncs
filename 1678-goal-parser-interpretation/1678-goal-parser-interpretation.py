class Solution:
    def interpret(self, command: str) -> str:
        pointer = 0
        result = ''
        while pointer < len(command):
            if command[pointer] == 'G':
                result += "G"
                pointer += 1
            elif command[pointer:pointer+2] == '()':
                result += "o"
                pointer += 2
            else:
                result += "al"
                pointer += 4
        return result