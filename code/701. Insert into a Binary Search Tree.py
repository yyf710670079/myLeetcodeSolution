# coding = utf-8
__author__ = "Yufeng Yang"
from my_class.binary_tree import BinaryTree, TreeNode

"""
Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

For example, 

Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5

You can return this binary search tree:

         4
       /   \
      2     7
     / \   /
    1   3 5

This tree is also valid:

         5
       /   \
      2     7
     / \   
    1   3
         \
          4


"""


# method 1
# Time: O(lgN)
# Space: O(1)
def insertIntoBST(self, root, val):
    """
    :param root: TreeNode
    :param val: int
    :return: TreeNode

    no two identical values
    and directly search the tree
    """

    if not root:
        return root

    real_root = root

    def traverse(root, val):
        if root.val < val:
            if root.right:
                traverse(root.right, val)
            else:
                root.right = TreeNode(val)
                return
        if root.val > val:
            if root.left:
                traverse(root.left, val)
            else:
                root.left = TreeNode(val)
                return

    traverse(real_root, val)

    return real_root


# simplify last solution
# suppose there are no identical values in different nodes
def insertIntoBST2(root, val):
    """
    :param root: TreeNode
    :param val: int
    :return: TreeNode

    no two identical values
    and directly search the tree
    """

    if root.val > val:
        if root.left:
            insertIntoBST2(root.left)
        else:
            root.left = TreeNode(val)

    else:
        if root.right:
            insertIntoBST2(root.right)
        else:
            root.right = TreeNode(val)

    return root





