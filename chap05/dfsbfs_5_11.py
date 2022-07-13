from collections import deque


def solution(maze):
    ways = [(0, 1), (0, - 1), (1, 0), (-1, 0)]
    n, m = len(maze), len(maze[0])

    visited = set()
    queue = deque([(0, 0)])
    while queue:
        for i in range(len(queue)):
            x, y = queue.popleft()
            visited.add((x, y))
            for way in ways:
                next_x, next_y = x + way[0], y + way[1]
                if (next_x, next_y) not in visited and 0 <= next_x < n and 0 <= next_y < m and maze[next_x][next_y] != 0:
                    maze[next_x][next_y] = maze[x][y] + 1
                    queue.append((next_x, next_y))

    return maze[n - 1][m - 1]


m1 = [[1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]

print(solution(m1))
