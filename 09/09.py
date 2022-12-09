def move(k1, k2):
    x1, y1 = k1
    x2, y2 = k2

    dx = x1 - x2
    dy = y1 - y2

    if abs(dx) > 1 or abs(dy) > 1:
        if dx == 0 or dy == 0:
            x2 += dx / 2
            y2 += dy / 2
        else:
            x2 += dx / abs(dx)
            y2 += dy / abs(dy)
    
    return (x2, y2)

def part1(x):
    hx, hy = 0, 0
    tx, ty = 0, 0

    t_pos = set()

    for d, n in x:
        for _ in range(int(n)):
            if d == 'R':
                hx += 1
            elif d == 'L':
                hx -= 1
            elif d == 'U':
                hy += 1
            elif d == 'D':
                hy -= 1

            tx, ty = move((hx, hy), (tx, ty))
            t_pos.add((tx, ty))

    return len(t_pos)

def part2(x):
    k = [(0, 0)] * 10

    t_pos = set()

    for d, n in x:
        for _ in range(int(n)):
            hx, hy = k[0]

            if d == 'R':
                hx += 1
            elif d == 'L':
                hx -= 1
            elif d == 'U':
                hy += 1
            elif d == 'D':
                hy -= 1
            
            k[0] = (hx, hy)

            for i in range(1, 10):
                k[i] = move(k[i - 1], k[i])
            
            t_pos.add(k[9])
    
    return len(t_pos)

with open('09.in') as f:
    s = f.read()
    x = [i.split() for i in s.splitlines()]

    print(part1(x))
    print(part2(x))
