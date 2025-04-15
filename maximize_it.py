from itertools import product

'''
1 to 7 lists, each list 1 to 7 elements, each element 1 to 10^9, M is 1000 or less
'''

''' 
    Test values - have to swap between
    "drop_the_first" comments.
K, M = 7, 671
inputt = [
    [7, 5678403, 6770488, 5713245, 6503478, 7774748, 5900452, 531896],
    [7, 7728332, 501199, 9141815, 7341382, 7238970, 8282671, 3037527],
    [7, 7763981, 7041667, 3521352, 9616160, 7322888, 5685405, 6017382],
    [7, 7278231, 1143649, 6460915, 8159948, 2436146, 1238439, 9869216],
    [7, 1422820, 9424407, 4982886, 7101222, 8711246, 696130, 6121051],
    [7, 6485993, 6596581, 9169298, 4214325, 7097779, 827465, 4072058],
    [7, 6853100, 9110135, 9625936, 7133432, 8668153, 5663640, 6749591]
]
'''
K, M = input().split()
K, M = int(K), int(M)
sequence_of_lists = []
for _ in range(K):
    sequence_in_list = []
    # I don't need the length of the line (the first value on this
    # line), because python - so I will drop it.
    drop_the_first = input().split()
    # drop_the_first = inputt[_]  # For testing purposes
    for _i in range(1, len(drop_the_first)):
        # Take each of the remaining elements and mod them and
        # square the result. This is a modular maximization problem
        # where 
        #   (x^2 + y^2 + z^2) mod M 
        # is equivalent to 
        #   ((x mod M)^2 + (y mod M)^2 + (z mod M)^2) mod M
        # The reason I want to do this is because numbers used here
        # are massive and their squares more so. They would take
        # forever to calculate out, so this is less computationally 
        # complex - and faster.
        sequence_in_list.append(((int(drop_the_first[_i]))%M)**2)
    sequence_of_lists.append(sequence_in_list)

# I don't know ahead of time which of the elements in each list will
# produce the best result - so I just make a list of every possible
# combination and check if they are the best answer
combies = list(product(*sequence_of_lists))
answer = 0
for row in combies:
    maybe = 0
    for element in row:
        maybe += element
    if maybe%M > answer:
        answer = maybe%M

print(answer)
