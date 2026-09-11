class Trienode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = Trienode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Trienode()

            curr = curr.children[ch]
        
        curr.is_end = True

    def search(self, word: str) -> bool:

        def helper(curr, position):
            if position == len(word):
                return curr.is_end

            ch = word[position]

            if ch == ".":
                for child in curr.children.values():
                    if helper(child, position+1):
                        return True
                return False

            if ch not in curr.children:
                return False

            return helper(curr.children[ch], position+1)

        return helper(self.root, 0)

                    