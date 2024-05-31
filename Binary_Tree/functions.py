from Trees.binary_tree import Node, BinaryTree


def delete(self, word):
        self.root = self._delete(self.root, word)

def _delete(self, node, word):
        if node is None:
            return node
        if word < node.word:
            node.left = self._delete(node.left, word)
        elif word > node.word:
            node.right = self._delete(node.right, word)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            node.word = self._find_max(node.left).word
            node.left = self._delete(node.left, node.word)
        return node

def _find_max(self, node):
        if node.right is None:
            return node
        else:
            return self._find_max(node.right)

def insert(self, word):
        if self.root is None:
            self.root = Node(word)
        else:
            self._insert(word, self.root)

def _insert(self, word, node):
        if word < node.word:
            if node.left is None:
                node.left = Node(word)
            else:
                self._insert(word, node.left)
        elif word > node.word:
            if node.right is None:
                node.right = Node(word)
            else:
                self._insert(word, node.right)

def find(self, word):
        if self.root is not None:
            return self._find(word, self.root)
        else:
            return None

def _find(self, word, node):
        if word == node.word:
            return node
        elif word < node.word and node.left is not None:
            return self._find(word, node.left)
        elif word > node.word and node.right is not None:
            return self._find(word, node.right)

def build_tree_from_file(filename):
    tree = BinaryTree()
    with open(filename, 'r') as file:
        for line in file:
            for word in line.split():
                tree.insert(word)
    return tree

def build_dict_from_file(filename):
    word_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            for word in line.split():
                word_dict[word] = True
    return word_dict

def search_word_in_dict(word_dict, word):
    return word_dict.get(word, False)

def search_word_in_file(filename, word):
    with open(filename, 'r') as file:
        for line in file:
            if word in line.split():
                return True
    return False
