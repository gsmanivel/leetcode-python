def finalVal():
    word1 = ["ab", "c"]
    word2 = ["a", "bc"]

    return "".join(word1) == "".join(word2)


if __name__ == '__main__':
    print(finalVal())

    # https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
