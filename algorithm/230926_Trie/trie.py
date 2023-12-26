class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
trie = Trie()

# 단어 삽입
trie.insert("apple")
trie.insert("app")
trie.insert("banana")

# 단어 검색
print(trie.search("apple"))    # True
print(trie.search("appl"))     # False
print(trie.search("app"))      # True

# 접두어로 시작하는 단어가 있는지 확인
print(trie.starts_with("ban")) # True
print(trie.starts_with("bat")) # False
