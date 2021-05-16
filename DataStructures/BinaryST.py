import json
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
        else:
            curr_node = self.root
            while True:
                if data >= curr_node.data:
                    if curr_node.right is None:
                        curr_node.right = newNode
                        return
                    curr_node = curr_node.right
                else:
                    if curr_node.left is None:
                        curr_node.left = newNode
                        return
                    curr_node = curr_node.left

    def lookup(self, data):
        if self.root is None:
            return False
        curr_node = self.root
        while curr_node is not None:
            if curr_node.data == data:
                return True
            elif data >= curr_node.data:
                curr_node = curr_node.right
            else:
                curr_node = curr_node.left
        return False



    def print_t1(self,curr):
        if curr is not None:
            self.print_t1(curr.left)
            print(curr.data)
            self.print_t1(curr.right)

    def print_tree1(self,tree):
        if tree.root is not None:
            self.print_t1(tree.root)






bst = BinaryST()
bst.insert(9)
bst.insert(5)
bst.insert(11)
bst.insert(2)
bst.insert(7)
bst.insert(14)

# bst.print_tree()

bst.print_tree1(bst)
print(bst.lookup(14))