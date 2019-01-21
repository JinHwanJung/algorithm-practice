# https://www.acmicpc.net/problem/2248
m = [[0]*9 for _ in range(32)]
# m[n][l] : n 자리의 이진수들 중에서 l개 이하의 비트만 1로 이루어진 이진수의 개수

def solution(n, l, i):
    # n: 이진수 최대 자릿수
    # l: 비트 '1' 의 최대개수
    # i: 몇번째 이진수를 구하는지
    pass

def bin_count(n, l):
    if m[n][l] != 0:
        return m[n][l]

    if n == 0:
        return 1
    if l == 0:
        return 1

    m[n][l] = bin_count(n-1, l-1) + bin_count(n-1, l)
    return m[n][l]


def test():
    print(bin_count(5, 3))
    assert solution(5, 3, 19) == "10011"
