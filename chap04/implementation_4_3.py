def solution(position):
    r, c = ord(position[0]) - 96, int(position[1])

    step1 = [(0, -2), (0, 2), (2, 0), (-2, 0)]
    step2 = [(0, -1), (0, 1), (1, 0), (-1, 0)]

    possible = 0
    for s1 in step1:
        for s2 in step2:
            new_position = (r + s1[0] + s2[0], c + s1[1] + s2[1])
            if ((s1[0] == 0 and s2[0] != 0) or (s1[0] != 0 and s2[0] == 0)) and 1 <= new_position[0] <= 8 and 1 <= new_position[1] <= 8:
                possible += 1

    return possible


p1 = "a1"
p2 = "c2"

print(solution(p1))
print(solution(p2))
