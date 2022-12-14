import ast
import functools

def compare(x, y):
    for xi, yi in zip(x, y):
        if type(xi) is int and type(yi) is int:
            if xi < yi:
                return -1
            elif xi > yi:
                return 1
        else:
            if type(xi) is not list:
                c = compare([xi], yi)
            elif type(yi) is not list:
                c = compare(xi, [yi])
            else:
                c = compare(xi, yi)

            if c:
                return c
    
    if len(x) < len(y):
        return -1
    elif len(x) > len(y):
        return 1
    
    return 0

def part1(x):
    l = [tuple(map(ast.literal_eval, i.splitlines())) for i in x.split('\n\n')]
    c = []

    for i, (x, y) in enumerate(l, start = 1):
        if compare(x, y) == -1:
            c.append(i)
    
    return sum(c)

def part2(x):
    l = [*map(ast.literal_eval, x.replace('\n\n', '\n').splitlines())] + [[[2]], [[6]]]

    s = sorted(l, key = functools.cmp_to_key(compare))

    return (s.index([[2]]) + 1) * (s.index([[6]]) + 1)

with open('input/13.in') as f:
    s = f.read()
    x = s

    print(part1(x))
    print(part2(x))
