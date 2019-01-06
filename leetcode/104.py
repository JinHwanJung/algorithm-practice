# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/?fbclid=IwAR15K0usEbQN7J9KXvFcQhOhTDBhLcpJyJ3yUcjucpqQDO0ol9GspN_qDgE
# 풀이완료


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        Time: O(N), Space: O(log(N))
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        if root is not None:
            stack.append((1, root))

        depth = 0
        while len(stack) != 0:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))

        return depth


def test():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)

    root2 = root.left
    root3 = root.right

    root2.left = None
    root2.right = None

    root3.left = TreeNode(15)
    root3.right = TreeNode(7)

    s = Solution()
    assert s.maxDepth(root) == 3
