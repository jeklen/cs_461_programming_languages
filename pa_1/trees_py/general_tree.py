class Tree(object):
    # generic tree node
    def __init__(self, name='root', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

t = Tree('*', [Tree('1'),
               Tree('2'),
               Tree('+', [Tree('3'),
                           Tree('4')])])
print(t.children)
