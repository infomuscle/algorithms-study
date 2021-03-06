def solution(n):
    # minute, second = 0, 0
    # mc_cnt = 0
    # while minute < 60:
    #     if "3" in str(minute) + str(second):
    #         mc_cnt += 1
    #     second += 1
    #     if second == 60:
    #         second = 0
    #         minute += 1
    #
    # three_cnt = 0
    # for i in range(n + 1):
    #     if "3" in str(i):
    #         three_cnt += 3600
    #     else:
    #         three_cnt += 1575  # mc_cnt
    #
    # return three_cnt
    return sum([3600 if "3" in str(i) else 1575 for i in range(n + 1)])


n1 = 5
print(solution(n1))
