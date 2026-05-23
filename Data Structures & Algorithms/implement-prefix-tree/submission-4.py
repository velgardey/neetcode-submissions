class TrieNode:

    def __init__ (self):
        self.children = {}
        self.eow = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.eow = True 

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True if cur.eow == True else False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True
        