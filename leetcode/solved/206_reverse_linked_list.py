# 풀이완료
# https://leetcode.com/problems/reverse-linked-list/?fbclid=IwAR1f32kFG7OK78GVBNB44eVN_0gW2VPgpkiB8-me-JUUJxZvqHfjKel0NKo


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        l = []
        node = head
        while True:
            l.append(node.val)
            node = node.next
            if node is None:
                break

        dummy_node = ListNode(0)
        ptr = dummy_node
        for n in reversed(l):
            ptr.next = ListNode(n)
            ptr = ptr.next

        return dummy_node.next


def stringToIntegerList(input):
    import json
    return json.loads(input)


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


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
            head = stringToListNode(line)
            ret = Solution().reverseList(head)

            out = listNodeToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
