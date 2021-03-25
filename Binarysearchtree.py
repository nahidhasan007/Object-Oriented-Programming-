class BstNode:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BstNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BstNode(data)

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements+=self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements+=self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)

        if self.left:
            elements+=self.left.pre_order_traversal()
        
        if self.right:
            elements+=self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements+=self.left.post_order_traversal()
        
        if self.right:
            elements+=self.right.post_order_traversal()
        
        elements.append(self.data)

        return elements

def BuildTree(elements):
    root = BstNode(elements[0])
    for data in elements:
        root.add_child(data)

    return root

datas = [20,7,9,12,45,36,77]
tree = BuildTree(datas)
print(tree.in_order_traversal())
print(tree.pre_order_traversal())
print(tree.post_order_traversal())