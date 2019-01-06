# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/?fbclid=IwAR06l-6l-H0Kbk5xDSOCkHWtasohU7gSJRY7qVYpgPGoLVtDWdGkeWl_WCE
import json


def stringToIntegerList(input):
    return json.loads(input)


def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);

            ret = Solution().sortedArrayToBST(nums)

            out = treeNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        pass