from collections import deque

class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = {}  


class Trie:
    def __init__(self):
        self.head = TrieNode()

    def insert(self, sentence):
        current = self.head
        for c in sentence:
            current = self.upsert(current, c, 1)

    def upsert(self, d, key, value):
        if key in d.children:
            d.children[key].count += value
        else:
            d.children[key] = TrieNode()
            d.children[key].count = value
        return d.children[key]

    def query(self, q):
        current = self.head
        try:
            for c in q:
                current = current.children[c]
            return current.count
        except KeyError:
            return 0


class TreeNode:
    def __init__(self):
        self.trie = Trie()
        self.children = []


class Tree:
    def __init__(self):
        self.treemap = {}  

    def add_node(self, parent, children):
        if parent not in self.treemap:
            self.treemap[parent] = TreeNode()
        self.treemap[parent].children += children

    def insert_sentence(self, nodename, sentence):
        self.treemap[nodename].trie.insert(sentence)

    def query(self, nodename, q):
        return self.treemap[nodename].trie.query(q)


class Ontology:
    def __init__(self):
        self.t = Tree()
        pass

    def parse_flat_tree(self, flat_tree):
        import copy
        s = copy.copy(flat_tree)
        words = deque(s.split(" "))
        root = words.popleft()
        if words.popleft() == '(':  
            self.parse_flat_tree_helper(self.t, root, words)
        return self.t

    def save_query(self, query):
        node, sentence = query.split(":")
        self.t.insert_sentence(node.strip(), sentence.strip())

    def find_query_count(self, matching_to):
        node, sep, query = matching_to.partition(" ")
        q = deque()
        q.append(node)
        count = 0
        while len(q) > 0:
            c = q.popleft()
            q.extend(self.t.treemap[c].children)
            count += self.t.query(c, query)
        return count

    def parse_flat_tree_helper(self, t, parent, words):
        current_word = words.popleft()
        children = []
        while current_word:
            if current_word == "(":
                self.parse_flat_tree_helper(t, previous_word, words)
                current_word = words.popleft()
            elif current_word == ")":
                if len(children) > 0:
                    t.add_node(parent, children)  
                break 
            else:
                children.append(current_word)
                t.add_node(current_word, [])  
                previous_word = current_word
                try:
                    current_word = words.popleft()
                except IndexError:
                    current_word = None


def main():
    o = Ontology()
    flat_tree_size = int(raw_input())
    flat_tree = raw_input()
    o.parse_flat_tree(flat_tree)
    given_query_count = int(raw_input())
    for i in range(0, given_query_count):
        o.save_query(raw_input())
    query_count = int(raw_input())
    for i in range(0, query_count):
        print o.find_query_count(raw_input())
    pass



if __name__ == '__main__':
    main()