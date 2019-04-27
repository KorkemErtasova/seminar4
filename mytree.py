class MyTree(object):
    def __init__(self, value):
        self.value = value
        self.l = None
        self.r = None
        self.count = 1

    def __str__(self):
        return 'value: {0}'.format(self.value)

def insert(root, value):
    if not root:
        return MyTree(value)
    elif root.value == value:
        root.count += 1
    elif value < root.value:
        root.l = insert(root.l, value)
    else:
        root.r = insert(root.r, value)
    return root

def search(root, word, dpt=1):
    if not root:
        return 0, 0
    elif root.value == word:
        return dpt, root.count
    elif word < root.value:
        return search(root.l, word, dpt + 1)
    else:
        return search(root.r, word, dpt + 1)

def create(seq):
    root = None
    for word in seq:
        root = insert(root, word)
    return root




def print_tree(root):
    if root:
        print_tree(root.l)
        print(root)
        print_tree(root.r)
