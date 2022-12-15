import re

def empty_ranges(x, ty):
    r = []

    for sx, sy, bx, by in x:
        d = abs(bx - sx) + abs(by - sy)
        dw = abs(ty - sy)

        if dw <= d:
            r.append([sx - d + dw, sx + d - dw])

    r.sort()
    i = 0

    while i < len(r) - 1:
        if r[i][1] >= r[i + 1][0] - 1:
            r[i][1] = max(r[i][1], r[i + 1][1])
            r.pop(i + 1)

            continue

        i += 1
    
    return r

def part1(x):
    return sum(i[1] - i[0] for i in empty_ranges(x, 2000000))

def part2(x):
    for ty in range(0, 4000001):
        r = empty_ranges(x, ty)

        if len(r) > 1:
            tx = r[0][1] + 1

            return tx * 4000000 + ty

with open('input/15.in') as f:
    s = f.read()
    x = [[*map(int, re.findall(r'(-?\d+)', l))] for l in s.splitlines()]

    print(part1(x))
    print(part2(x))