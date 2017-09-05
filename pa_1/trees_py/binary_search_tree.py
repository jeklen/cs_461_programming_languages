# binary_search_tree
class Node:
    """
    Tree node: left and right child + data which can be any object
    """
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        """
        Insert new node with data
        @param data node data object to insert
        """
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def lookup(self, data, parent=None):
        """
        Loopup node containing data
        @param data node data object to look up
        @param parent node's parent
        @returns node and node's parent if found or None, None
        """
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent

    def children_count(self):
        """
        return the number of children
        @return number of children: 0, 1, 2
        """
        cnt = 0
        if self.left:
            cnt = cnt + 1
        if self.right:
            cnt = cnt + 1
        return cnt

    def delete(self, data):
        """
        Delete node containing data
        @param data node's content to delete
        """
        # get node containing data
        node, parent = self.lookup(data)
        if node is not None:
            children_count = node.children_count
        if children_count == 0:
            # if node has no children, just remove it
            if parent:
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
                del Node
            else:
                self.data = None
        elif children_count == 1:
            # if node has 1 child
            # replace node with its child
            if node.left:
                n = node.left
            else:
                n = node.right
            if parent:
                if parent.left is node:
                    parent.left = n
                else:
                    parent.right = n
                del node
            else:
                self.left = n.left
                self.right = n.right
                self.data = n.data

root = Node(8)
root.insert(3)
root.insert(10)
root.insert(1)
root.insert(6)
root.insert(4)
root.insert(7)
root.insert(14)
root.insert(13)
node, parent = root.lookup(6)
print(node)
print(node.data)
print(parent.data)
