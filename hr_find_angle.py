# Find the angle
# Given that angle ABC is 90degrees & M is the midpoint between A & C, what is MBC for a particular AB & BC?
# Output: Nearest integer

from math import degrees, atan

# Because the midpoint M is at a right angle, the angle BAC is going to be the 
# same as the angle from MBC. Since we know AB (adjecent) and BC (opposite), we 
# can use atan to find that angle, which is the same as the angle that this 
# challenge is looking for.
adj = int(input())
opp = int(input())
x=round(degrees(atan(adj/opp)))
print(f"{x}{chr(176)}")
