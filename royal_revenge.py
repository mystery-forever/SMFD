MOD = 10**9 + 7
max_steps = 100

paths = [[0] * (max_steps + 1) for _ in range(max_steps + 1)]
paths[0][0] = 1

for x in range(1, max_steps + 1):
    for y in range(x + 1):
        total = paths[x-1][y]
        if y > 0:
            total += paths[x][y-1]
        paths[x][y] = total % MOD

results = [paths[n][n] for n in range(1, max_steps + 1)]
print(results)
