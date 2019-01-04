# https://leetcode.com/problems/move-zeroes/?fbclid=IwAR3oreFVWpz-o0l2jO3d4nCBhJKexo_OF9G-qZAv-Jwoyyopt7_9HFFRiCc
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_count = nums.count(0)
        for _ in range(zero_count):
            nums.remove(0)
            nums.append(0)

    # def moveZeroes2(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: void Do not return anything, modify nums in-place instead.
    #     """
    #     pass

def test():
    s = Solution()
    l = [0, 1, 0, 3, 12]
    s.moveZeroes(l)
    assert l == [1, 3, 12, 0, 0]

# def test2():
#     s = Solution()
#     l = [0, 1, 0, 3, 12]
#     s.moveZeroes(l)
#     assert l == [1, 3, 12, 0, 0]