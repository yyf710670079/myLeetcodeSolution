# coding = utf-8
__author__ = "Yufeng Yang"
from my_class.binary_tree import TreeNode, BinaryTree
import time

"""
A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Return a list of all possible full binary trees with N nodes. 
 
Each element of the answer is the root node of one possible tree.

Each node of each tree in the answer must have node.val = 0.

You may return the final list of trees in any order.

 

Example 1:

Input: 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],
        [0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
"""


# Time: O(2^n)
def allPossibleFBT(N):
    """
    :param N: int
    :return: List[TreeNode]

    explanation:
        Recursively construct the tree that satisfy the specifications
    """

    N -= 1
    if N == 0:
        return [TreeNode(0)]

    ans = []
    for l in range(1, N, 2):
        for left in allPossibleFBT(l):
            for right in allPossibleFBT(N - l):
                root = TreeNode(0)
                root.left = left
                root.right = right
                ans.append(root)

    return ans


# simplified version
class Solution(object):
    def __init__(self):
        self.cache = dict()

    def allPossibleFBT2(self, N):
        """
        :param N: int
        :return: List[TreeNode]
        """

        if N in self.cache:
            return self.cache[N]

        N -= 1
        if N == 0:
            return [TreeNode(0)]

        ans = []
        for l in range(1, N, 2):
            for left in self.allPossibleFBT2(l):
                for right in self.allPossibleFBT2(N - l):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    ans.append(root)

        self.cache[N] = ans
        return ans


if __name__ == "__main__":
    t1 = Solution()
    tick = time.time()
    t1_ans = t1.allPossibleFBT2(19)
    tock = time.time()
    print("\ncache solution time: %.3f ms" % ((tock-tick)*1000))

    tick2 = time.time()
    t2_ans = allPossibleFBT(19)
    tock2 = time.time()
    print("\nrecursive solution time: %.3f ms" % ((tock2 - tick2) * 1000))


    # assert(len(t1_ans) == )
    for root in t1_ans:
        assert(BinaryTree.is_full_binary_tree(root))

