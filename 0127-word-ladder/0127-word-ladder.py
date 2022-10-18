'''
It's a combination of building the adjacency list after which we're gonna perform the BFS, since we have to find the shortest
possible path. The logic here will be to build an adjacency matrix to O(nm2) where n is the number of words and m is the length of each word (usually it is O(n2m)). After since it’s the shortest path question, it’s best to use BFS (O(n2m)).
'''
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # check whether the endword even exists in the wordlist or not
        if endWord not in wordList:
            return 0
        
        # Building Adjacency List
        
        neighbours = collections.defaultdict(list) # we create an empty list default dict to prepare the adjacency list.
        wordList.append(beginWord) # we first append the beginning word to the wordlist.
        for word in wordList: # traverse through the words
            for j in range(len(word)): # traverse through each of the word inside the list ( <= 10 in size constraint)
                pattern = word[:j] + "*" + word[j+1:]
                '''
                Here we create wildcard substituted patterns for example hot :
                *ot
                h*t
                ho*
                after which we can create and match the other patterns (single letter difference)
                '''
                neighbours[pattern].append(word)
        
        # Start with BFS!
        
        
        # Maintaining a set of visited words when we perform BFS.
        visited = set([beginWord]) 
        # Intializing the queue for the BFS operations with beginning word.
        q = deque([beginWord])
        # Store the length of atleast the beginning word ie. 1 inside a result varaible.
        result = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    # if we arrive at the endword, we return the length of path
                    return result
                for j in range(len(word)): # traverse through each of the word inside the list ( <= 10 in size constraint)
                    pattern = word[:j] + "*" + word[j+1:]
                    for neighbourWord in neighbours[pattern]:
                        # for all the neighbourword existing in the neighbours dictionary, with keys as the patterns
                        if neighbourWord not in visited:
                            visited.add(neighbourWord)
                            q.append(neighbourWord)
            result+=1
        return 0
        