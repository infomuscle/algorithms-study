import random


def solution1(nums, m, k):
    nums.sort(reverse=True)
    return sum([__num_decision(i, k, nums[0], nums[1]) for i in range(m)])


def __num_decision(i, k, first, second):
    return second if (i + 1) % (k + 1) == 0 else first


def solution2(nums, m, k):
    nums.sort(reverse=True)
    count_of_unit = m // (k + 1)
    value_of_unit = nums[0] * k + nums[1]
    remain = m - (k + 1) * count_of_unit

    return value_of_unit * count_of_unit + nums[0] * remain


n1 = [2, 4, 5, 4, 6]
m1 = 8
k1 = 3

n2 = [3, 5, 7, 2, 4, 6, 8, 3, 5, 7, 9, 3, 4, 5, 7, 8]
m2 = 9
k2 = 5

for i in range(100):
    rm = random.randrange(10000) + 1
    rk = random.randrange(10000) + 1
    s11, s12 = solution1(n1, rm, rk), solution2(n1, rm, rk)
    s21, s22 = solution1(n2, rm, rk), solution2(n2, rm, rk)
    if s11 != s12:
        print("s11, s12: ", s11, s12)
    if s21 != s22:
        print("s21, s22: ", s21, s22)
