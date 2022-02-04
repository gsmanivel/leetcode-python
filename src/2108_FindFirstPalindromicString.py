def finalVal():
    words = ["abc","car","ada","racecar","cool"]

    for word in words:
        if word == word[::-1]:
            return word
    return ""


if __name__ == '__main__':
    print(finalVal())

    # https://leetcode.com/problems/find-first-palindromic-string-in-the-array/
