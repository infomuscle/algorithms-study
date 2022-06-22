import random


def solution1(n, k):
    cnt = 0
    while n > 1:
        if n % k == 0:
            n //= k
        else:
            n -= 1
        cnt += 1

    return cnt


def solution2(n, k):
    cnt = 0
    while n > 1:
        mod = n % k
        if mod == 0:
            n //= k
            cnt += 1
        else:
            n -= mod
            cnt += mod
    if n == 0:
        cnt -= 1

    return cnt


n1, k1 = 25, 5
n2, k2 = 25, 3
n3, k3 = 27, 3
n4, k4 = 70, 34

print(solution2(n1, k1))
print(solution2(n2, k2))
print(solution1(n3, k3))
print(solution2(n4, k4))

for i in range(100):
    n = random.randrange(100000) + 2
    k = random.randrange(n) + 2
    s1, s2 = solution1(n, k), solution2(n, k)
    if s1 != s2:
        print(n, k)
        print("s1, s2: ", s1, s2)
#
