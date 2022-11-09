class Solution:
    def rotateTheBox(self, box):
        '''
        stone - "#"
        stationary obstacle - "*"
        empty - "."
        '''
        # no changes to the horizontal positions
        # it is guaranteed that each stone in box will rest on an obstacle,
        # another stone or the bottom of the box
        for i in box:
            sticks_and_stones_hash = 0
            empty_dots = 0
            pointer = 0
            for index,j in enumerate(i):
                if j == "*": # Terminating condition.
                    i[pointer:index] = ["."]*empty_dots+["#"]* sticks_and_stones_hash
                    pointer = index+1
                    empty_dots = 0
                    sticks_and_stones_hash = 0
                elif j=="#":
                    sticks_and_stones_hash+=1
                else:
                    empty_dots+=1
            i[pointer:len(i)] = ["."]*empty_dots+["#"]* sticks_and_stones_hash
        return map(list, zip(*box[::-1]))