

def solution(A, B):
    A = abs(A)
    B = abs(B)
    if (A == B) and (B in [1, 2]):
        return 4
    if (A + B) == 1:
        return 3

    biggest_div = max(A/2, B/2, (A+B)/3)

    return biggest_div + ((biggest_div + A + B) % 2)

print(solution(1, 4))

# -100 000...100 000
