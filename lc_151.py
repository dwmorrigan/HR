# Given an input string s, reverse the order of the words.

class Solution:
    def reverseWords(self, s: str) -> str:
        new_word = []
        # Python makes this feel like cheating. Split the space-seperated words into a list and strip the extraneous spaces left.
        words = s.strip().split()
        # Going backwords through the list, add each word to a new list
        for i in range(len(words)-1, -1, -1):
            new_word.append(words[i])
        # Use ' '.join to add a space between each word to create the new string
        return ' '.join(new_word)

def main():
    x = Solution()
    s = "  the   sky  is  blue "
    assert x.reverseWords(s) == "blue is sky the"


if __name__ == "__main__":
    main()
