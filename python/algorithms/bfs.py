from logging import root


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preOrder(root: TreeNode):
    if not root: 
        return
    print(root.val, end ="")
    preOrder(root.left)
    preOrder(root.right)

def inOrder(root: TreeNode):
    if not root:
        return;
    inOrder(root.left)
    

def levelOrder(root: TreeNode) -> None:
    pass

def main() ->None:
    pass

if __name__ == "__main__":
    main()