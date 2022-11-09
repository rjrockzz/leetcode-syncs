class Solution:
    '''
       * Grouping of the characters
       * If groups occur more than 10 characters in length, split them
       * Do this in-place
       '''
    def compress(self, chars) -> int:
        cur_element = chars[0]
        num_element  = 1
        pointer = 0
        i = 1
        while i<len(chars):
            if chars[i]==cur_element:
                num_element+=1 
                i+=1               
            else:
                if num_element==1:
                    chars[:] = chars[:pointer]+[cur_element] + chars[i:]
                    pointer+=1
                    cur_element = chars[pointer]
                    num_element=1
                    i=pointer+1
                else:
                    chars[:] = chars[:pointer]+[cur_element] + list(str(num_element)) + chars[i:]
                    pointer+=2
                    cur_element = chars[pointer]
                    num_element=1
                    i=pointer+1
            
        if num_element==1:
            chars[:] = chars[:pointer]+[cur_element]
        else:
            chars[:] = chars[:pointer]+[cur_element] +list(str(num_element))
        return len(chars)
