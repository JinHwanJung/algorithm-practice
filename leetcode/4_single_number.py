# 풀이완료
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = dict()
        for n in nums:
            try:
                hash_table.pop(n)
            except:
                hash_table[n] = 1
        return list(hash_table.popitem())[0]


def test():
    s = Solution()
    assert s.singleNumber([2,2,1]) == 1
    assert s.singleNumber([4, 1, 2, 1, 2]) == 4
