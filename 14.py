def gen_walls(w):
    o = set()

    for p in w:
        for (a, b) in zip(p, p[1:]):
            x1, x2 = sorted([a[0], b[0]])
            y1, y2 = sorted([a[1], b[1]])

            for y in range(y1, y2 + 1):
                for x in range(x1, x2 + 1):
                    o.add((x, y))
    
    return o

def part1(x):
    o = gen_walls(x)
    g = 0

    while True:
        sx, sy = (500, 0)

        while True:
            if not [y for (x, y) in o if y >= sy]:
                return g

            if (sx, sy + 1) in o:
                if (sx - 1, sy + 1) in o:
                    if (sx + 1, sy + 1) in o:
                        o.add((sx, sy))
                        g += 1

                        break
                    else:
                        sx += 1
                else:
                    sx -= 1

            sy += 1

def part2(x):
    o = gen_walls(x)
    g = 0
    f = max(y for _, y in o) + 2

    while (500, 0) not in o:
        sx, sy = (500, 0)

        while True:
            if sy == f - 1:
                o.add((sx, sy))
                g += 1

                break

            if (sx, sy + 1) in o:
                if (sx - 1, sy + 1) in o:
                    if (sx + 1, sy + 1) in o:
                        o.add((sx, sy))
                        g += 1

                        break
                    else:
                        sx += 1
                else:
                    sx -= 1
                    
            sy += 1

    return g

with open('input/14.in') as f:
    s = f.read()
    x = [[[*map(int, c.split(','))] for c in i.split(' -> ')] for i in s.splitlines()]

    print(part1(x))
    print(part2(x))