# Take a string and split it into substrings, each of the same length
# s = string
# n = length of s
# k = a factor of n
# Within each substrung, allow on the first occurance of each letter. 
# Print out the new substring, each on a new line.

def merge_the_tools(string, k):
    # your code goes here
    chunks = [string[i:i+k] for i in range(0, len(string), k)]
    for chunk in chunks:
        unique = []
        for character in chunk:
            unique.append(character if character not in unique else '')
        print(''.join(unique))

if __name__ == '__main__':
#    string, k = "AABCAAADA", 3
    string, k = input(), int(input())
    merge_the_tools(string, k)