def solution(n: int):
    coins = [500, 100, 50, 10]

    changes = 0
    for coin in coins:
        changes += n // coin
        n %= coin

    return changes


n1 = 1260
print(solution(n1))

# Given the number of coin types is K, time complexity is O(K). It isn't affected by N, the amount of money.
