from collections import deque

'''
There is a horizontal row of  cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if cube[i] is on top of cube[j] then sideLength[j] >= sideLength[i].

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print Yes if it is possible to stack the cubes. Otherwise, print No.

Choose blocks from right OR left in order to successfully stack the blocks.

Input Format
The first line contains a single integer , the number of test cases.
For each test case, there are  lines.
The first line of each test case contains , the number of cubes.
The second line contains  space separated integers, denoting the sideLengths of each cube in that order.

Output Format
For each test case, output a single line containing either Yes or No
'''

def order(row):
    front_index = 0
    back_index = len(row)-1
    tower = []
    for i in range(back_index+1):
        
        if row[front_index] >= row[back_index]:
            tower.append(row[front_index])
            front_index += 1
        elif row[back_index] > row[front_index]:
            tower.append(row[back_index])
            back_index = back_index - 1
        else:
            print("Ohno")
        # If the tower has more than one block on it, then check to see 
        # if the top block is bigger than the penultimate block
        if len(tower) > 1 and tower[-2] < tower[-1]:
            print("No")
            return
    print("Yes")
    return

# Sadly, I'm out time for this one at the moment. While order() is correct, tower() is not yet.
def tower(row):
    # d = deque([4, 3, 2, 1, 3, 4])
    # d = deque([1, 3, 2])
    d = deque(row)
    pile = 9**9
    while pile > 0:
        if d[0] >= d[-1] and d[0] <= pile:
            pile = d.popleft()
        elif d[0] < d[-1] and d[-1] <= pile:
            pile = d.pop()
        else:
            pile = 0
            print("No")
            break
        if len(d) < 1:
            pile = 0
            print("Yes")


def main():

    T = int(input())
    list_of_cubes = []
    for i in range(T):
        _ = input()
        list_of_cubes.append(list(map(int, input().strip().split())))

    for row in list_of_cubes:
        order(row)
        tower(row)


if __name__ == "__main__":
    main()

'''
3
6
4 3 2 1 3 4
3
1 3 2
7
4 3 4 1 2 3

'''