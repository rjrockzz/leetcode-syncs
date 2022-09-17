class Solution:
    def ispalin(self, s):  # check if a string is palin (s is suffix of word in our case)
        return s == s[::-1]

    def palindromePairs(self, words):
        result = []
        root = {}  # use dict instead of a TrieNode class to save space
        for i, word in enumerate(words):
            curr = root
            for idx, ch in enumerate(word):
                if ch not in curr:
                    curr[ch] = {}
                curr = curr[ch]
                tmp = word[idx+1:]
                if tmp and self.ispalin(tmp):
                    # keep the idx of word if the suffix of the word after current position is palin
                    curr.setdefault("ids", []).append(i)
            curr["isword"] = i  # keep idx of word when reach the end
        for j, word in enumerate(words):  # start searching reverse of each word in the Trie
            w = word[::-1]
            curr = root
            fail = False
            for idx, ch in enumerate(w):
                if ch not in curr:
                    fail = True
                    break
                curr = curr[ch]
                # if current node is the end of some word, check whether the suffix of reverse word is palin
                i = curr.get("isword")
                if i is not None and i != j and self.ispalin(w[idx+1:]):
                    result.append([i, j])
            if not fail and "ids" in curr:
                result.extend([i, j] for i in curr["ids"] if i != j)
        if "" in words:  # check for "" case
            idx = words.index("")
            result.extend(reduce(lambda x, y: x + y, ([[i, idx], [idx, i]] for i, w in enumerate(words) if w and self.ispalin(w))))
        return result