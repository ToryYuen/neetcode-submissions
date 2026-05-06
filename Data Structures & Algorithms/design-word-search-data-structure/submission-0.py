class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_word = True
        

    def search(self, word: str) -> bool:
        
        def dfs(idx:int, node:TrieNode) -> bool:
            curr = node
            for i in range(idx, len(word)):
                c = word[i]
                if c == '.':
                    return any([dfs(i + 1, suffix_node) for suffix_node in curr.children.values()])
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.is_word

        return dfs(0, self.root)
        
