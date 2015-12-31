# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

test_array = [
    [5, 5, 1, 7, 2, 3, 5],
    [1, 1, 1, 1, 1, 1],
    [5, 5, 5, 5, 5, 5, 5]

]


def solution(X, A):
    same_count = A.count(X)
    diff_count = 0
    index = -1

    while same_count != diff_count and index != len(A) - 1:

        index += 1

        if A[index] == X:
            same_count -= 1
        else:
            diff_count += 1

    result = index + 1

    return result


for a in test_array:
    print(solution(5, a))
