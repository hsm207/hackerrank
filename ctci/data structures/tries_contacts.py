# Problem description: https://www.hackerrank.com/challenges/ctci-contacts/problem


class TrieNode:
    def __init__(self):
        # a map from a character to a child
        self.children = {}
        self.size = 0

    def putChildIfAbsent(self, ch):
        if ch not in self.children:
            self.children[ch] = TrieNode()

    def getChild(self, ch):
        return self.children[ch]


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        current_node = self.root

        for ch in word:
            current_node.putChildIfAbsent(ch)
            current_node = current_node.getChild(ch)
            current_node.size += 1

    def find(self, prefix):
        current_node = self.root
        for ch in prefix:
            if ch not in current_node.children:
                return 0
            else:
                current_node = current_node.getChild(ch)

        return current_node.size


trie = Trie()
# trie.add('hello')
# trie.add('helicopter')
# trie.find('hel')

n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == 'add':
        trie.add(contact)
    else:
        print(trie.find(contact))
