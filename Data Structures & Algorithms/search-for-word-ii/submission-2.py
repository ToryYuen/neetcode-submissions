class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_word = False

    def addWord(self, word: str) -> None:
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        DIRECTION = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        res, visited = set(), set()

        def dfs(r: int, c: int, curr:TrieNode, word) -> None:
            if (r < 0 or r >= ROWS 
                or c < 0 or c >= COLS
                or (r, c) in visited
                or board[r][c] not in curr.children):
                    return

            visited.add((r, c))
            curr = curr.children[board[r][c]]
            word += board[r][c]
            if curr.is_word:
                res.add(word)

            for x, y in DIRECTION:
                dfs(r + x, c + y, curr, word)
            visited.remove((r, c))

        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, root, "")
        return list(res)