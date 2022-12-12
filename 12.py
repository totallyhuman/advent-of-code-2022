def height(l):
    return 'SabcdefghijklmnopqrstuvwxyzE'.index(l)

def neighbors(x, r, c):
    p = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
    w = len(x[0])
    h = len(x)

    return [(r_, c_) for r_, c_ in p if 0 <= r_ < h and 0 <= c_ < w]

def shortest(x, s):
    e = [(p, 0) for p in s]
    v = []

    while e:
        (r, c), l = e.pop(0)

        if x[r][c] == 'E':
            return l

        if (r, c) in v:
            continue
        
        v.append((r, c))
        
        for (r_, c_) in neighbors(x, r, c):
            if height(x[r_][c_]) <= height(x[r][c]) + 1:
                e.append(((r_, c_), l + 1))

def part1(x):
    w = len(x[0])
    h = len(x)

    s = [(r, c) for r in range(h) for c in range(w) if x[r][c] == 'S']

    return shortest(x, s)

def part2(x):
    w = len(x[0])
    h = len(x)

    s = [(r, c) for r in range(h) for c in range(w) if x[r][c] == 'a']

    return shortest(x, s)

with open('input/12.in') as f:
    s = f.read()
    x = s.splitlines()

    print(part1(x))
    print(part2(x))
