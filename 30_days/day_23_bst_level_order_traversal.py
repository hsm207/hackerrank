class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def levelOrder(self, root):
        queue = [root]

        while queue:
            node = queue.pop(0)
            print(node.data, end=" ")
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)


T = [3, 5, 4, 7, 2, 1]
myTree = Solution()
root = None
for i in T:
    root = myTree.insert(root, i)
myTree.levelOrder(root)
