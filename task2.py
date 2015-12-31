from math import ceil

v = [1, 1, 1, 0, 0, 1, 1]

a = sum([v[i] * (-2)**i for i in xrange(len(v))])

print a

b = -a


# var negabinary = [];
#         var base = -2;
#         var remainder;
#
#         while(decimal != 0) {
#
#             remainder = decimal % base;
#             decimal = Math.ceil(decimal / base);
#             negabinary.push(remainder >= 0 ? remainder : -remainder);
#         }
#
#         return negabinary.reverse().join('');


def negabinary(val):
    arr = []
    base = -2
    while val != 0:
        remainder = val % base
        val = ceil(float(val) / float(base))
        arr.append(abs(int(remainder)))

    return arr


v = negabinary(b)
print(v)

a = sum([v[i] * (-2)**i for i in xrange(len(v))])

print a
