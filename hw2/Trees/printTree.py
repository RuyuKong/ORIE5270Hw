from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getHeight(self, root):
        if not root:
            return 0
        left = self.getHeight(root.left)
        right = self.getHeight(root.right);
        return 1 + max(left, right);

    def bfs(self, left, right, root, res):

        queue = deque()
        queue.append([root, left, right, 0]) # node, start, end, level
        while queue:
            node, left, right, level = queue.popleft()
            mid = int(left + (right-left)/2)
            res[level][mid] = str(node.val)
            if node.left:
                queue.append([node.left, left, mid, level+1])
            if node.right:
                queue.append([node.right, mid, right, level+1])
        for row in res:
            print(row)

    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        treeHeight = self.getHeight(root)
        columns = (1 << treeHeight) - 1
        res = [[""] * columns for x in range(treeHeight)]
        self.bfs(0, columns, root, res)
        return res
