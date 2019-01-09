# coding = utf-8
__author__ = "Yufeng Yang"
from my_class.binary_tree import BinaryTree

"""
We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.

Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

Example 1:
Input: [1,null,0,0,1]
Output: [1,null,0,null,1]

         1
       /   \                  ---------\                  1
    None     0                          \                   \
           /   \                        /                     0
         0       1            ---------/                        \
                                                                  1

 
Explanation: 
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.


"""


# Time: O(N)
# Space: O(H) H means the height of the tree
def pruneTree(root):
    """
    :param root: TreeNode
    :return: TreeNode

    If the root.left subtree only has 0, then we just return None. Otherwise, we can prune the sub tree recursively.
    """

    if not root:
        return root

    if only_zero_in(root.left):
        root.left = None
    else:
        root.left = pruneTree(root.left)

    if only_zero_in(root.right):
        root.right = None
    else:
        root.right = pruneTree(root.right)

    return root


def only_zero_in(root):
    if not root:
        return True

    if root.val == 1:
        return False

    if root.val == 0:
        return only_zero_in(root.left) and only_zero_in(root.right)

# simplified version
def pruneTree2(root):
    """
    :param root: TreeNode
    :return: TreeNode

    """

    if not root:
        return root
    root.left, root.right = pruneTree2(root.left), pruneTree2(root.right)
    return root if root.val == 1 or root.left or root.right else None


if __name__ == "__main__":
    t1_tree = BinaryTree([1, None, 0, 0, 1])
    t1_tree_ans = BinaryTree([1, None, 0, None, 1])
    t1_tree.print_tree(t1_tree.get_head())
    print("")
    t1_tree_ans.print_tree(t1_tree_ans.get_head())
    t1_new_head = pruneTree(t1_tree.get_head())
    print("")
    BinaryTree.print_tree(t1_new_head)
    print("")
    # t1_new_head2 = pruneTree2()
    assert (BinaryTree.is_identical(t1_new_head, t1_tree_ans.get_head()))





