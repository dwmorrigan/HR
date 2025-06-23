# Integer Palindrome
# Must only use one line with a single print statement to create a triangle of 
# integer palindromes
# Input: 1 - 9
# Output: (example: 5)
# 1
# 121
# 12321
# 1234321
# 123454321

# I did not appreciate this one - it's a neat math trick, but is essentially 
# irrelevant to learning Python. The trick is that 1*1=1, 11*11=121, 
# 111*111=12321. If you know that, and remember a prior HR challenge that used 
# 10**i//9 to create a table of 1s, then you can combine them for the solution.

for i in range(1,int(input())+1):
    print(((10**i)//9)**2)
