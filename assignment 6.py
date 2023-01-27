#ans1
def is_perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum == n:
        return True
    else:
        return False

#ans2
v=input("Write any Word:-")
if v==v[::-1]:
    print("The word is a Palindrome!")
else:
    print("The word is not a Palindrome")

#ans3
def pascal_triangle(n):
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j])
        pascal_triangle.append(row)
    for i in range(n):
        print(pascal_triangle[i])

#ans4
import string
def is_pangram(s):
    s = s.lower()
    alphabet = set(string.ascii_lowercase)
    s = ''.join(c for c in s if c.isalpha())
    unique_chars = set(s)
    if unique_chars == alphabet:
        return True
    else:
        return False

#ans5
def sort_hyphen_separated_words(s):
    words = s.split("-")
    words.sort()
    sorted_string = '-'.join(words)
    print(sorted_string)

#ans8
class SumToZero:
    def __init__(self, numbers):
        self.numbers = numbers
    def find_triplets(self):
        self.numbers.sort()
        for i in range(len(self.numbers) - 2):
            if self.numbers[i] > 0:
                break
            if i > 0 and self.numbers[i] == self.numbers[i - 1]:
                continue
            l, r = i + 1, len(self.numbers) - 1
            while l < r:
                s = self.numbers[i] + self.numbers[l] + self.numbers[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    print("Triplet found:", self.numbers[i], self.numbers[l], self.numbers[r])
                    return (self.numbers[i], self.numbers[l], self.numbers[r])
        print("No triplet found that sums to zero.")

#ans9
class Parentheses:
    def __init__(self, string):
        self.string = string
    def is_valid(self):
        stack = []
        for char in self.string:
            if char in "([{":
                stack.append(char)
            elif char in ")]}":
                if not stack:
                    return False
                if char == ")" and stack[-1] != "(":
                    return False
                if char == "]" and stack[-1] != "[":
                    return False
                if char == "}" and stack[-1] != "{":
                    return False
                stack.pop()
        return not stack