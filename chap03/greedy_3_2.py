def solution(nums, m, k):
    nums.sort(reverse=True)
    return sum([num_decision(i, k, nums[0], nums[1]) for i in range(m)])


def num_decision(i, k, first, second):
    return first if i == 0 or i % k != 0 else second


n1 = [2, 4, 5, 4, 6]
m1 = 8
k1 = 3

print(solution(n1, m1, k1))
