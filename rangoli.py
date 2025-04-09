def print_rangoli(size):
    # your code goes here
    if size == 0:
        return
    sub = size - 1
    first = "--"*sub + chr(size+96) + "--"*sub
    modulate = list(first)
    pattern = [first]
    grow = 0
    for entry in range(1, size):
        now = modulate[2*sub]
        if now == 'a':
            grow = 2
        modulate[2*sub] = chr(ord(now)-1+grow)
        how_many = size - (ord(modulate[2*sub]) - 96)
        for loops in range(how_many):
            next_letter = ((2*sub)-(2*(loops+1)))+2
            this_letter = chr(ord(modulate[next_letter])+1)
            modulate[(2*sub)-(2*(loops+1))] = this_letter
            modulate[(2*sub)+(2*(loops+1))] = this_letter
        result = ''.join(map(str, modulate))
        pattern.append(result)
    for entry in range(sub, 0, -1):
        pattern.append(pattern[entry-1])

    for entry in pattern:
        print(entry)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)