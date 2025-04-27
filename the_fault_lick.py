from collections import defaultdict

n, m = map(int, input().split())
A = [input() for x in range(n)]
B = [input() for x in range(m)]

'''
5 4
a
a
b
a
b
a
b
c
b
'''
d = defaultdict(list)

for index, letter in enumerate(A):
    d[letter].append(index)

for letter in B:
    if letter in A:
        for x in d[letter]:
            print(x+1, end=' ')
    else:
        print(-1, end='')
    print()

# I'm not happy with this one. It does what is asked of it, but I am certain it could be done neater and more 'pythonic'. 