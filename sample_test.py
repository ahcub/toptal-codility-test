
a = [-1, 3, -4, 5, 1, -6, 2, 1]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = [2, -1, -2, 1, 500]


def solution(A):
    if not A or not isinstance(A, (list, tuple)):
        return -1

    left_sum = 0
    right_sum = sum(A[1:])
    equilibrium_index = 0
    while left_sum != right_sum:
        if equilibrium_index >= len(A) - 1:
            return -1

        left_sum += A[equilibrium_index]
        right_sum -= A[equilibrium_index+1]
        equilibrium_index += 1

    return equilibrium_index


print(solution(a))
