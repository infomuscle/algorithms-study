def solution(position):
    r, c = ord(position[0]) - 96, int(position[1])

    steps = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, -2), (1, 2), (-1, 2), (-1, -2)]

    possible = 0
    for step in steps:
        new_position = (r + step[0], c + step[1])
        if 1 <= new_position[0] <= 8 and 1 <= new_position[1] <= 8:
            possible += 1

    return possible


p1 = "a1"
p2 = "c2"

print(solution(p1))
print(solution(p2))
