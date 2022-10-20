class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        target_number = second_number = first_number = "" 
        for i in firstWord:
            first_number+=str(abs(97-ord(i)))
        for i in secondWord:
            second_number+=str(abs(97-ord(i)))
        for i in targetWord:
            target_number+=str(abs(97-ord(i)))
        if int(first_number)+int(second_number)==int(target_number):
            return True
        else:
            return False