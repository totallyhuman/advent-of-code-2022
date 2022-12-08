def north(x, r, c):
    return [x[r1][c] for r1 in range(0, r)[::-1]]

def west(x, r, c):
    return [x[r][c1] for c1 in range(0, c)[::-1]]

def south(x, r, c):
    return [x[r1][c] for r1 in range(r + 1, len(x))]

def east(x, r, c):
    return [x[r][c1] for c1 in range(c + 1, len(x))]

def part1(x):
    total = 0

    for r in range(len(x)):
        for c in range(len(x)):
            t = x[r][c]

            if all(t > b for b in north(x, r, c)) or \
               all(t > b for b in west(x, r, c)) or \
               all(t > b for b in south(x, r, c)) or \
               all(t > b for b in east(x, r, c)):
                total += 1
    
    return total


def part2(x):
    sc = [[0 for _ in range(len(x))] for _ in range(len(x))]

    for r in range(len(x)):
        for c in range(len(x)):
            t = x[r][c]

            n = 0
            for b in north(x, r, c):
                n += 1
                
                if t <= b:
                    break
            
            w = 0
            for b in west(x, r, c):
                w += 1
                
                if t <= b:
                    break
            
            s = 0
            for b in south(x, r, c):
                s += 1
                
                if t <= b:
                    break
            
            e = 0
            for b in east(x, r, c):
                e += 1

                if t <= b:
                    break
            
            sc[r][c] = n * w * s * e
    
    return max(map(max, sc))

with open('08.in') as f:
    s = f.read()
    x = [[int(i) for i in l] for l in s.splitlines()]

    print(part1(x))
    print(part2(x))
