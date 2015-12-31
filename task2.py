from math import ceil

v = [1, 1, 1, 0, 0, 1, 1]

a = sum([v[i] * (-2)**i for i in xrange(len(v))])

print a

b = -a


def int_to_negabinary(val):
    working_val = float(val)
    arr = []
    base = -2
    while working_val != 0:
        bit = working_val % base
        working_val = ceil(working_val / base)
        arr.append(abs(int(bit)))

    return arr


v = int_to_negabinary(b)
print(v)

a = sum([v[i] * (-2)**i for i in xrange(len(v))])

print a
