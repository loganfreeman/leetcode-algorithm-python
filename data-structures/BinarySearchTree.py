class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        """
        insert data into the tree, return true if inserted, else false
        """
        ''' For inserting the data in the Tree '''
        if self.data == data:
            return False        # As BST cannot contain duplicate data

        elif data < self.data:
            ''' Data less than the root data is placed to the left of the root '''
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True

        else:
            ''' Data greater than the root data is placed to the right of the root '''
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def minValueNode(self, node):
        if node is None:
            return None
        current = node
        while(current.leftChild is not None):
            current = current.leftChild

        return current

    def delete(self, data):
        if self is None:
            return None
        if data < self.data:
            self.leftChild = self.leftChild.delete(data)
            return self
        elif data > self.data:
            self.rightChild = self.rightChild.delete(data)
            return self
        else:
            if self.leftChild is None:
                temp = self.rightChild
                self = None
                return temp
            elif self.rightChild is None:
                temp = self.leftChild
                self = None
                return temp
            else:
                temp = self.minValueNode(self.rightChild)
                self.data = temp.data
                self.rightChild = self.rightChild.delete(temp.data)
                return self

    def find(self, data):
        if(self.data == data):
            return self
        elif data < self.data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return None
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return None

    def preorder(self):
        if self:
            print(str(self.data), end=" ")
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.data), end=" ")
            if self.rightChild:
                self.rightChild.inorder()

    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.data), end=" ")


class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def delete(self, data):
        if self.root:
            return self.root.delete(data)

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return None

    def preorder(self):
        if self.root:
            self.root.preorder()

    def postorder(self):
        if self.root:
            self.root.postorder()

    def inorder(self):
        if self.root:
            self.root.inorder()


if __name__ == '__main__':
    tree = Tree()
    tree.insert(10)
    tree.insert(12)
    tree.insert(5)
    tree.insert(4)
    tree.insert(20)
    tree.insert(8)
    tree.insert(7)
    tree.insert(15)
    tree.insert(13)
    print(tree.find(1))
    print(tree.find(12))
    ''' Following tree is getting created:
                    10
                 /      \
               5         12
              / \           \
            4     8          20
                 /          /
                7         15
                         /
                       13
    '''

    tree.preorder()
    tree.inorder()
    tree.postorder()
    print('\n\nAfter deleting 20')
    tree.delete(20)
    tree.inorder()
    tree.preorder()
    print('\n\nAfter deleting 10')
    tree.delete(10)
    tree.inorder()
    tree.preorder()
