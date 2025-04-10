from stopwatch import Stopwatch

def possibleChanges(usernames):
    # Write your code here
    array = []
    for name in usernames:
        name_list = list(name)
        ordered_names = name_list[:]
        ordered_names.sort()
        if ordered_names == name_list:
            array.append("NO")
        else:
            array.append("YES")
    return array

def stringAnagram(dictionary, query):
    # Write your code here
    anagrams = []
    new_dict = []
    expanded_dict = [list(x.strip()) for x in dictionary]
    for word in expanded_dict:
        word.sort()
        new_word = ''.join(word)
        new_dict.append(new_word)
    for word in query:
        counter = 0
        word_expanded = list(word.strip())
        word_expanded.sort()
        new_word = ''.join(word_expanded)
        if new_word in new_dict:
            counter = new_dict.count(new_word)
        anagrams.append(counter)
    return anagrams

def ana(dict, query):
    anagrams = []
    for word in query:
        counter = 0
        for entry in dict:
            if sorted(word) == sorted(entry):
                counter += 1
        anagrams.append(counter)
    return anagrams

# def solve(s):
#     return capped = ' '.join([x.title() if not x[0].isdigit() else x for x in s.split()])

def solve(s):
    names = ""
    z = ''
    space = False
    for x in range(len(s)):
        if x == 0:
            if s[x].isdigit():
                names += s[x]
            else:
                z = s[x].upper()
                names += z
        elif s[x].isspace():
            names += s[x]
            space = True
        elif s[x].islower() and space == True:
            z = s[x].upper()
            names += z
            space = False
        else:
            names += s[x]
            space = False
    return names

def ssss(s):
    return ' '.join(word[:1].upper() + word[1:] if word else '' for word in s.split(' '))


if __name__ == "__main__":
    result = possibleChanges(["aaaba", "superhero", "ace"])
    print(result)
    dictionary = ['hack', 'a', 'rank', 'khac', 'ackh', 'kran', 'rankhacker', 'a', 'ab', 'ba', 'stairs', 'raits']
    query = ['a', 'nark', 'bs', 'hack', 'stair']
    sw = Stopwatch(9)
    sw.start()
    result = stringAnagram(dictionary, query)
    print(result)
    print(str(sw))
    sw.reset()
    sw.start()
    result = ana(dictionary, query)
    print(result)
    print(str(sw))
    print(solve("12asdlkj brando"))
    print(solve("asd addd add"))
    print(solve("1 2 2 3 4 5 6 7 8  9"))
    print(ssss("12asdlkj brando"))
    print(ssss("asd addd add"))
    print(ssss("1 2 2 3 4 5 6 7 8  9"))