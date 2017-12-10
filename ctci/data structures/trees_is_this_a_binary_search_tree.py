# Problem description: https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


def check(node, min, max):
    if node is None:
        return True
    if node.data <= min or node.data >= max:
        return False
    # when doing left check, the minimum is the grandparent's value
    # and the max is the parent's value
    left_check = check(node.left, min, node.data)
    right_check = check(node.right, node.data, max)
    return left_check and right_check


def checkBST(root):
    return check(root, 0, 10e4)
