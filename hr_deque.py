from collections import deque

def main():
    # N = int(input())
    # n = list()
    # for x in range(N):
    #     n.append(input().split())
    N = 6
    n = [['append', '1'], ['append', '2'], ['append', '3'], ['appendleft', '4'], ['pop'], ['popleft']]
    d = deque()
    for x in n:
        if x[0] == 'append':
            d.append(x[-1])
        elif x[0] == 'appendleft':
            d.appendleft(x[-1])
        elif x[0] == 'clear':
            d.clear()
        elif x[0] == 'extend':
            d.extend(x[-1])
        elif x[0] == 'extendleft':
            d.extendleft(x[-1])
        elif x[0] == 'count':
            d.count(x[-1])
        elif x[0] == 'pop':
            d.pop()
        elif x[0] == 'popleft':
            d.popleft()
        elif x[0] == 'remove':
            d.remove(x[-1])
        elif x[0] == 'reverse':
            d.reverse()
        elif x[0] == 'rotate':
            d.rotate(x[-1])
        else:
            print("something went wrong")
            return
    for x in d:
        print(x, end=' ')

if __name__ == "__main__":
    main()