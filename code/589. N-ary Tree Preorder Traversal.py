# coding = utf-8
__author__ = "Yufeng Yang"

"""
Given an n-ary tree, return the preorder traversal of its nodes' values.

For example, given a 3-ary tree:

              1
           /  |  \
        3     2    4
      /   \
    5       6

 

Return its preorder traversal as: [1,3,5,6,2,4].
"""


# Time: O(n) n is the number of the TreeNode
# Space: O(n) n is the number of the TreeNode
class Solution(object):
    def __init__(self):
        self.ans = []

    def preorder(self, root):
        """
        :param root: Node
        :return: List[int]

        Recursive solution
        """

        if root:
            self.ans.append(root.val)

            for child in root.children:
                self.preorder(child)

        return self.ans


# Iterative solution
class Solution2(object):
    def __init__(self):
        self.ans = []
        self.stack = []

    def preorder(self, root):
        """
        :param root: Node
        :return: List[int]
        """
        if not root:
            return self.ans

        self.stack.append(root)

        while self.stack:
            root = self.stack.pop()
            self.ans.append(root.val)

            # from right to left
            for child in root.children[::-1]:
                self.stack.append(child)

        return self.ans

