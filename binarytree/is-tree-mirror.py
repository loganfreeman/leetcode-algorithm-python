class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def isMirror(root1, root1):
    if root1 is None and root2 is None:
        return True
    """
    for two trees to be mirror images, the following three conditions must
    be true:
    1. Their root node's key must be same
    2. left subtree of left tree and right subtree of right tree have to be mirror image
    3. right subtree of left tree and left subtree of right tree have to be mirror image
    """
    if (root1 is not None and root2 is not None):
        if root1.key == root2.key:
            return isMirror(root1.left, root2.right) and
                isMirror(root1.right, root2.right)
    return False

def isSymmetric(root):
    return isMirror(root, root)