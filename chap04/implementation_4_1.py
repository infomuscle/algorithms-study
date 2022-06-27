def solution(n, plan):
    directions = {
        "R": (0, 1),
        "L": (0, -1),
        "U": (-1, 0),
        "D": (1, 0)
    }

    current = (1, 1)
    for p in plan:
        next_x, next_y = current[0] + directions[p][0], current[1] + directions[p][1]
        if 1 <= next_x <= n and 1 <= next_y <= n:
            current = (next_x, next_y)

    return current


n1, p1 = 5, ["R", "R", "R", "U", "D", "D"]

print(solution(n1, p1))
