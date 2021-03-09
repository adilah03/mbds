### Question 1 ###

# needed for ceiling function
import math

# get min sum that can be calculated from matrix
def get_min_sum(m, n):
    return int((m ** 2 + m + 2 * n - 2) / 2)

# get max sum that can be calculated from matrix
def get_max_sum(m, n):
    return int((m ** 2 + (2 * m * n) - m) / 2)

# get sequence of numbers that gives us minimum sum
# i.e., R till the top right corner and then D till the bottom right corner
# this will be treated as our base sequence
def get_min_seq(m, n):
    s = [1] * (n - 1)
    for k in range(1, m + 1):
        s.append(k)
    return s

# get sequence of number that gives us wanted sum
def get_seq(m, n, s):
    # get base sequence for this matrix
    seq = get_min_seq(m, n)
    min_sum = get_min_sum(m, n)
    # find how much the sum differs from the minimum
    diff = s - min_sum
    if s == min_sum:
        return seq
    else:
        # in order to make up the difference,
        # calculate how many '1's in the base sequence are to be replaced by m
        # (since m is the biggest number in the matrix)
        quotient = math.ceil(diff / (m - 1)) - 1
        for j in range(quotient):
            seq.remove(1)
            seq.append(m)
        # find the remainder and add it to the sequence
        # by removing another '1' and adding (remainder + 1)
        remainder = diff % (m - 1)
        if remainder == 0:
            seq.remove(1)
            seq.append(m)
        else:
            seq.remove(1)
            seq.append(remainder + 1)
        # sort the sequence to get the right order
        seq.sort()
        return seq


def get_direction(m, n, s):
    # check that sum can even be calculated from the matrix
    min_sum = get_min_sum(m, n)
    max_sum = get_max_sum(m, n)
    if s < min_sum:
        print(str(s) + ' Sum is smaller than the minimum (' + str(min_sum) + ') for a ' + str(m) + 'x' + str(n) + ' matrix')
    elif s > max_sum:
        print(str(s) + ' Sum is bigger than the maximum (' + str(max_sum) + ') for a ' + str(m) + 'x' + str(n) + ' matrix')
    # convert sequence of numbers to directions
    # if consecutive numbers are the same, it means we go R
    # else, it means we go D
    else:
        seq = get_seq(m, n, s)
        direction = ''
        for h in range(len(seq) - 1):
            if seq[h] == seq[h + 1]:
                direction += 'R'
            else:
                direction += 'D'
        print(str(s) + ' ' + direction)

# 1a)
for i in [65, 72, 90, 110]:
    get_direction(9, 9, i)

print('')

# 1b)
for i in [87127231192, 5994891682]:
    get_direction(90000, 100000, i)
