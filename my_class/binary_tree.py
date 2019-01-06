# coding=utf-8
__author__ = "Yufeng Yang"


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, lst):
        self.head = TreeNode(lst[0])
        q = [self.head]

        # point to the value of the lst
        i = 1
        N = len(lst)
        while q:
            q_tmp = []
            for node in q:
                if node is not None:
                    if i < N:
                        if lst[i]:
                            node.left = TreeNode(lst[i])
                            q_tmp.append(node.left)
                        i += 1

                    if i < N:
                        if lst[i]:
                            node.right = TreeNode(lst[i])
                            q_tmp.append(node.right)
                        i += 1

            q = q_tmp

    def get_head(self):
        return self.head




