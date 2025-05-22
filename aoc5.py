''' 
    2025-05-08
    This one is kind of ugly and I kind of don't care. This is Advent of Code 2025 day 5.
    * Part 1: This pure stumped me when I tried to do it in December. The fact that it is working now is enough for me and I'm moving on to see if I can't make it further "this year" than I have in the past.
    * Part 2: I think I can just "catch" the bad books and toss them to a seperate function that fixes the order and returns the corrected book?

    Take set of updates as subset from total order - this should be an acyclic diagraph that can have an actual first page and last page.
'''
from collections import defaultdict, deque
from stopwatch import Stopwatch

def get_input(file_name):
    pages = {}
    books = []
    with open(file_name) as f:
        # page order info is '|' bar seperated while the pages of each book are
        # ',' comma seperated.
        # Thus, pages is a directed graph with each node (page) connected by a
        # vertex indicating page order primacy
        for line in f:
            if '|' in line:
                a, b = line.strip().split('|')
                if a not in pages:
                    pages[a] = []
                if b not in pages:
                    pages[b] = []
                pages[a].append(b)
            elif ',' in line:
                books.append(line.strip().split(','))
    return pages, books

def the_real_order(rules):
    inDegree = defaultdict(int)
    for  neighbors in rules.values():
        for neighbor in neighbors:
            temp = inDegree[neighbor] + 1
            inDegree[neighbor] = temp
    linedup = deque([i for i in rules if inDegree[i] == 0])
    result = []
    while linedup:
        v = linedup.popleft()
        result.append(v)
        for neighbor in rules[v]:
            inDegree[neighbor] -= 1
            if inDegree[neighbor] == 0:
                linedup.append(neighbor)
    return result

def valid_order(rules, updates):
    # I wonder which is more efficient. Passing the information once and just
    # looping through it or calling the function for each update?
    middles = []
    for update in updates:
        # Dict of the order/position (by index) for each page of the update
        pos = { page: i for i, page in enumerate(update)}
        # Toggle to jump out of bad books. If this was a one update at a time
        # function, then it could just be a return statement with the middle
        # value.
        good = True
        for page in update:
            # Check each "I go first" vertex for each node in the graph
            for after in rules[page]:
                # Not all "I go first"es will be in an update. Skip those that
                # aren't
                if after in pos:
                    # And, of course, if the order doesn't follow the rules,
                    # this is a bad bad book, so ban it.
                    if pos[after] < pos[page]:
                        good = False
                        break
        # The book isn't banned, get the middle page and add it to a list
        if good:
            middles.append(int(update[len(update)//2]))
    return middles

def find_subset(cyclic_graphs, acyclic_input):
    # Cyclic is updates
    # Acyclic is rules
    # sub_set is only the rules that are needed for an update
    acyclic_output = []
    for row in cyclic_graphs:
        sub_set = {}
        for before, after in acyclic_input.items():
            if before in row:
                # Only append those values that are also in row
                ss = set(row) & set(after)
                sub_set[before] = list(ss)
        acyclic_output.append(sub_set)
    return acyclic_output

def main():
    sw = Stopwatch()
    sw.start()
    filename = "aoc5.1.txt" 
    rules, updates = get_input(filename)
    print(sum(valid_order(rules, updates))) # Part 1: 6041
    # Get update subset of rules - make function.
    sub_graph = find_subset(updates, rules)
    middle_pages = 0
    for i in range(len(sub_graph)):
        ordered = the_real_order(sub_graph[i]) 
        if ordered != updates[i]:
            middle_pages += int(ordered[len(ordered)//2])
    print(middle_pages) # Part 2: 4884
    sw.stop()
    print(sw)

if __name__ == "__main__":
    main()