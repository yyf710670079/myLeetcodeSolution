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
                        if lst[i] is not None:
                            node.left = TreeNode(lst[i])
                            q_tmp.append(node.left)
                        i += 1

                    if i < N:
                        if lst[i] is not None:
                            node.right = TreeNode(lst[i])
                            q_tmp.append(node.right)
                        i += 1

            q = q_tmp

    def get_head(self):
        return self.head

    @classmethod
    def is_identical(cls, root1,root2):
        if root1 and root2:
            if root1.val == root2.val:
                return cls.is_identical(root1.left, root2.left) and cls.is_identical(root1.right, root2.right)
            else:
                return False

        if root1 is None and root2 is None:
            return True
        else:
            return False

    # def print_tree(self):
    #     if self.head:
    #         print("[", end="")
    #         q = [self.head]
    #         while q:
    #             q_tmp = []
    #             for node in q:
    #                 print(node.val, end=", ")
    #                 if node.left:
    #                     q_tmp.append(node.left)
    #                     # print(node.left.val, end=" ")
    #                 else:
    #                     print("None", end=", ")
    #
    #                 if node.right:
    #                     q_tmp.append(node.right)
    #                     # print(node.right.val, end=" ")
    #                 else:
    #                     print("None", end=", ")
    #
    #             q = q_tmp
    #
    #         print("]", end="")
    #
    #     else:
    #         print("[]")

    @classmethod
    def print_tree(cls, root):
        if root is not None:
            print(root.val, end=" ")

        if root.left is not None or root.right is not None:
            if root.left is not None:
                cls.print_tree(root.left)
            else:
                print("None", end=" ")

            if root.right is not None:
                cls.print_tree(root.right)
            else:
                print("None", end=" ")











