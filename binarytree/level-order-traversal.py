class Node:

    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def levelOrderTraversalUsingQueue(root):
    if root is None:
        return
    queue = []
    queue.append(root)

    while(len(queue) > 0):
        # Print front of queue and remove it from queue
        print (queue[0].data)
        node = queue.pop(0)

        #Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)

def levelOrderTravesal(root):
    h = height(root)
    for i in range(1, h+1):
        printGivenLevel(root, i)

def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end = " ")
    elif leve > 1:
        printGivenLevel(root.left, level -1)
        printGivenLevel(root.right, level -1)
def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1