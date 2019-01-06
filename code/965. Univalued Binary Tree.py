# coding = utf-8
__author__ = "Yufeng Yang"
from my_class.binary_tree import BinaryTree

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


# DFS method
# Time: O(n)
def isUnivalTree2(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    ans = []

    def dfs(root):
        if root:
            ans.append(root.val)
            dfs(root.left)
            dfs(root.right)

    dfs(root)
    return len(set(ans)) == 1


if __name__ == "__main__":
    t1 = [1, 1, 1, 1, 1, None, 1]
    t2 = [1, 1, 1, 1, 1, None, 2]
    t1_tree = BinaryTree(t1)
    t1_head = t1_tree.get_head()

    t2_head = BinaryTree(t2).get_head()

    assert(isUnivalTree(t1_head))
    assert(not isUnivalTree(t2_head))
    assert(isUnivalTree2(t1_head))
    assert(not isUnivalTree2(t2_head))
    print("=========Pass all test cases=========")

