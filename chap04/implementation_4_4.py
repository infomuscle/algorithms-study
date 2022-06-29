def solution(map, position, face):
    way_map = {
        0: (-1, 0),
        1: (0, 1),
        2: (1, 0),
        3: (0, -1)
    }

    current_x, current_y = position[0], position[1]
    map[current_x][current_y] = 1
    visited = 1

    turns = 0
    while True:
        face = turn_left(face)
        next_x, next_y = current_x + way_map[face][0], current_y + way_map[face][1]
        if map[next_x][next_y] == 0 and 0 <= next_x < len(map) and 0 <= next_y < len(map[0]):
            visited += 1
            map[next_x][next_y] = 1
            current_x, current_y = next_x, next_y
            turns = 0
        else:
            turns += 1
            if turns == 4:
                back = way_back(face)
                current_x += way_map[back][0]
                current_y += way_map[back][1]
                if map[current_x][current_y] == 1 or current_x < 0 or current_x >= len(map) or current_y < 0 or current_y >= len(map[0]):
                    break

    return visited


def turn_left(face):
    face -= 1
    if face < 0:
        face = 3
    return face


def way_back(face):
    face += 2
    return face % 4


m1 = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]
p1 = (1, 1)
f1 = 0

print(solution(m1, p1, f1))
