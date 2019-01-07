# coding = utf-8
__author__ = "Yufeng Yang"
from my_class.binary_tree import TreeNode

"""
 Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

    The root is the maximum number in the array.
    The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
    The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.

Construct the maximum tree by the given array and output the root node of this tree.

Example 1:

Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1

"""


# Time: O(NlgN)
# Space: O(lgN)
def constructMaximumBinaryTree(nums):
    """
    :param nums: List[int]
    :return: TreeNode

    in every sub list, we search for the maximum value
    """
    N = len(nums)
    if N == 0:
        return None
    if N == 1:
        return TreeNode(nums[0])

    max_num = nums[0]
    max_index = 0

    for i in range(1, N):
        if nums[i] > max_num:
            max_num = nums[i]
            max_index = i

    root = TreeNode(nums[max_index])

    root.left = constructMaximumBinaryTree(nums[:max_index])
    root.right = constructMaximumBinaryTree(nums[max_index + 1:])

    return root


# Time: O(N)
# Space: O(N)
def constructMaximumBinaryTree(nums):
    """
    :param nums: List[int]
    :return: TreeNode

    We maintain a stack and scan all the numbers.
    In reality, if we meet a sub list decreasing, we keep append the number into the stack and stack[-1].right = cur

    If we meet a big number bigger than the last number in the stack, we keep popping the number until we find a value
    bigger than it. If we cannot find such one number, we just cur.left = stack[0] and pop all numbers because stack[0]
    is always the biggest.
    """
    stack = []

    for val in nums:
        cur = TreeNode(val)

        while stack and stack[-1].val < val:
            cur.left = stack.pop()

        if stack:
            stack[-1].right = cur

        stack.append(cur)

    return stack[0]


