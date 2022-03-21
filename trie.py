# Time  ：2022-3-9 8:06
# Author：Houtaroy

class Trie:

    def __init__(self):
        self.root = {}
        self.word_end = -1

    def insert(self, word):
        cur_node = self.root
        for c in word:
            if c not in cur_node:
                cur_node[c] = {}
            cur_node = cur_node[c]
        cur_node[self.word_end] = True

    def search(self, word):
        cur_node = self.root
        for c in word:
            if c not in cur_node:
                return False
            cur_node = cur_node[c]
        if self.word_end not in cur_node:
            return False
        return True

    def start_with(self, prefix):
        cur_node = self.root
        for c in prefix:
            if c not in cur_node:
                return False
            cur_node = cur_node[c]
        return True

if __name__ == '__main__':
    word = 'telephone'
    word_2 = 'test'
    prefix = 'tel'
    trie = Trie()
    trie.insert(word)
    trie.insert(word_2)
    print(trie.search(word))
    print(trie.search(word_2))
    print(trie.start_with(prefix))
