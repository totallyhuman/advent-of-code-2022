def part1(x):
    total = 0

    for i in x:
        e = ({*i[:len(i) // 2]} & {*i[len(i) // 2:]}).pop()

        total += 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(e) + 1
    
    return total

def part2(x):
    total = 0

    for i in range(0, len(x), 3):
        b = ({*x[i]} & {*x[i + 1]} & {*x[i + 2]}).pop()

        total += 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(b) + 1
    
    return total

with open('03.in') as f:
    s = f.read()
    x = s.splitlines()

    print(part1(x))
    print(part2(x))