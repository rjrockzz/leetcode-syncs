class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        h = {"1": 'A', "2": 'B',"3": 'C',"4": 'D',"5": 'E',"6": 'F',"7": 'G',"8": 'H',"9": 'I',"10": 'J',"11": 'K',"12": 'L',"13": 'M',"14": 'N',"15": 'O',"16": 'P',"17": 'Q',"18": 'R',"19": 'S',"20": 'T',"21": 'U',"22": 'V',"23": 'W',"24": 'X',"25": 'Y',"26": 'Z'}
        
        # O(2^N) time, O(N) space DFS solution. Caching reduces it to O(N) time
        @cache
        def traverse(i):
            if i >= n: return 1
            
            ans = 0
            if s[i] in h: ans += traverse(i + 1)
            if i + 1 < n and s[i] + s[i + 1] in h: ans += traverse(i + 2)
            return ans
                
        return traverse(0)
    
        # O(N) time, O(1) space DP solution
    
        a, b, c = 0, 1, 0
        
        for i in range(n - 1, -1, -1):
            if s[i] in h: a += b
            if i < n - 1 and s[i:i + 2] in h: a += c
            a, b, c = 0, a, b
            
        return b