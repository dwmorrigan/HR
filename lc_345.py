# Swap vowel pairs from the edges towards the center. Both upper and lowercase
# Moderately happy with this one as my first attempt works. Could be faster.

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        front = 0
        back = len(s) - 1
        f_s = ''
        b_s = ''
        while front < back:
            if s[front] in vowels and s[back] in vowels:
                # Do swap and advance
                f_s += s[back]
                b_s = s[front] + b_s
                front += 1
                back -= 1
            else:
                if s[front] not in vowels:
                    f_s += s[front]
                    front += 1
                if s[back] not in vowels:
                    b_s = s[back] + b_s
                    back -= 1
        if front == back:
            f_s += s[front]
        new_s = f_s + b_s
        return new_s


def main():
    x = Solution()
    s = "IceCreAm"
    print(x.reverseVowels(s)) # AceCreIm
    s = "leetcode"
    print(x.reverseVowels(s)) # leotcede


if __name__ == "__main__":
    main()
