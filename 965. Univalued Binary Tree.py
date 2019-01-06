# coding = utf-8
__author__ = "Yufeng Yang"

"""
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.


Example 1:
Input: [1,1,1,1,1,null,1]
Output: true
"""


# BFS method
# Time: O(n) n is the number of the nodes in the tree
def isUnivalTree(root):
    """
    :param root: TreeNode
    :return: bool
    """
    if not root:
        return True

    uni = root.val

    q = [root]

    while q:
        children = []
        for n in q:
            if n.val != uni:
                return False
            if n.left:
                children.append(n.left)
            if n.right:
                children.append(n.right)
        q = children

    return True