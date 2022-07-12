def solution(tray):
    cnt = 0
    for i in range(len(tray)):
        for j in range(len(tray[i])):
            if tray[i][j] == 0:
                dfs(i, j, tray)
                cnt += 1

    return cnt


def dfs(x, y, tray):
    if not (0 <= x < len(tray) and 0 <= y < len(tray[0])):
        return
    if tray[x][y] == 1:
        return

    tray[x][y] = 1

    dfs(x + 1, y, tray)
    dfs(x - 1, y, tray)
    dfs(x, y + 1, tray)
    dfs(x, y - 1, tray)


t1 = [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]

print(solution(t1))
