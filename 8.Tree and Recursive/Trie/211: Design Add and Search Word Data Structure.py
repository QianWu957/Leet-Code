class WordDictionary:
    def __init__(self):
        self.root = {}
        self.end = 'end'

    def addWord(self, word: str) -> None:
        curNode = self.root
        for c in word:
            if c not in curNode:
                curNode[c] = {}
            curNode = curNode[c]
        curNode[self.end] = {}


    def search(self, word: str) -> bool:
        def helper(word, tree):
            if not word:
                if self.end in tree:
                    return True
                return False
            
            if word[0] == '.':
                for c in tree:
                    if helper(word[1:], tree[c]):
                        return True
            

            elif word[0] in tree:
                if helper(word[1:], tree[word[0]]):
                    return True
            return False

        return helper(word, self.root)


       



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)