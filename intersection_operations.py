# Find the intersection of two sets

def intersections(m, c):
    o = m.strip().split()
    d = c.strip().split()
    s = set(o)
    return len(s.intersection(d))

if __name__ == '__main__':
    n = 9
    m = "1 2 3 4 5 6 7 8 9 1 1"
    b = 9
    c = "10 1 2 3 11 21 55 6 1 8"
#    n = input()
#    m = input()
#    b = input()
#    c = input()
    print(intersections(m, c))