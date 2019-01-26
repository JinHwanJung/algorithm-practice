def solution(l, v):
    v = sorted(v)
    print(v)
    size_v = len(v)
    max_d = 0
    for i in range(size_v-1):
        max_d = max(max_d, v[i+1]-v[i])
    max_d = max(max_d, l-v[-1])
    max_d = max(max_d, v[0])
    return int((max_d/2)+0.5)
