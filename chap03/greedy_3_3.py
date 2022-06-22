def solution(cards):
    choice = 0
    for row in cards:
        choice = max(choice, min(row))

    return choice


c1 = [[3, 1, 2], [4, 1, 4], [2, 2, 2]]
c2 = [[7, 3, 1, 8], [3, 3, 3, 4]]

print(solution(c1))
print(solution(c2))
