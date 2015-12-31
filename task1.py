# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

# A - not-empty array of integers
# X - integer
# N - size of array A
# 0 <= K <= N
# X in [0..K-1] == !X in [K..N-1]
# if K == 0 then [0..K-1] is empty
# if K == N then [K..N-1] is empty

test_array = [
    [5, 5, 1, 7, 2, 3, 5],  # X in [0..K-1] == !X in [K..N-1], K == 4
    [1, 15, 5, 51, 4, 7, 9, 1, 3, 4, 5, 8, 9, 6, 3, 5, 4, 7, 6, 5, 5],  # X in [0..K-1] == !X in [K..N-1], K == 4
    [1, 1, 1, 1, 1, 1],  # [0..K-1] is empty
    [5, 5, 5, 5, 5, 5, 5]  # [K..N-1] is empty

]


def solution(X, A):
    x_count = A.count(X)
    if x_count in [0, len(A)]:
        return x_count

    same_count = 0
    diff_count = len(A) - x_count
    index = 0

    while same_count != diff_count and index != len(A) - 1:
        if A[index] == X:
            same_count += 1
        else:
            diff_count -= 1
        index += 1

    return index


for a in test_array:
    print(solution(5, a))
