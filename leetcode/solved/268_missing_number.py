# https://leetcode.com/problems/missing-number/?fbclid=IwAR2HXcr4mKsUZ4GypIBlWkEXtqyvjX94K0GuVZZOsNnmNQKvFdVRmavcXlo
import json

# 풀이완료
# class Solution:
#     def missingNumber(self, nums):
#         return sum(range(0, len(nums)+1)) - sum(nums)

# Approach #1 Shorting
# class Solution:
#     def missingNumber(selfs, nums):
#         nums.sort()
#
#         # Ensure that n is at the last index
#         if nums[-1] != len(nums):
#             return len(nums)
#         # Ensure that 0 is at the first index
#         elif nums[0] != 0:
#             return 0
#
#         # if we get here, then the missing number is on the range(0, n)
#         for i in range(1, len(nums)):
#             excepted_num = nums[i-1]+1
#             if nums[i] != excepted_num:
#                 return excepted_num

# Approach #2 HashSet
# class Solution:
#     def missingNumber(self, nums):
#         num_set = set(nums)
#         n = len(nums) + 1
#         for number in range(n):
#             if number not in num_set:
#                 return number

# Approach #3 Bit Manipulation

def stringToIntegerList(input):
    return json.loads(input)


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

            ret = Solution().missingNumber(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
