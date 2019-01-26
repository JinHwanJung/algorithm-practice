def solution(arrA, arrB):
    size_arrA = len(arrA)
    for _ in range(size_arrA):
        arrA.append(arrA.pop(0))
        if arrA == arrB:
            return True
    return False
