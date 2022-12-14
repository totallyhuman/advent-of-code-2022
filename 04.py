def part1(x):
    total = 0

    for ((p1x, p1y), (p2x, p2y)) in x:
        r1 = {*range(p1x, p1y + 1)}
        r2 = {*range(p2x, p2y + 1)}

        if r1 & r2 in [r1, r2]:
            total += 1
    
    return total

def part2(x):
    total = 0

    for ((p1x, p1y), (p2x, p2y)) in x:
        r1 = {*range(p1x, p1y + 1)}
        r2 = {*range(p2x, p2y + 1)}

        if r1 & r2:
            total += 1
    
    return total

with open('input/04.in') as f:
    s = f.read()
    x = [[[*map(int, j.split('-'))] for j in i.split(',')] for i in s.splitlines()]

    print(part1(x))
    print(part2(x))
