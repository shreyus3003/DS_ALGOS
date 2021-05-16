def solution(A):
    # write your code in Python 3.6
    map = {}
    for i in range(len(A)):
        least = A[i] - 1
        if least <= 0:
            continue
        # arr.append(least)
        if least not in map:
            map[A[i]] = least
    print(map)
    # for j in range(len(A)):
    #     if A[j] not in arr.values():
    #         seen =
    # return seen

# def solution(A):
#     A.sort()
#     print(A)
#
#     return False
A = [1, 3, 6, 4, 1, 2]
res = solution(A)
print(res)