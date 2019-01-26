def solution(board, nums):
    N = len(board)
    answer = 0
    search = set(nums)
    for row in board:
        filtered = filter(lambda x: x in search, row)
        if len(filtered) == N:
            answer += 1

    return answer
