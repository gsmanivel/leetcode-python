def finalVal():
    allowed = "ab"
    words = ["ad", "bd", "aaab", "baa", "badab"]

    count = 0
    for word in words:
        flag = True
        for char in word:
            if allowed.find(char) == -1:
                flag = False;
                break
        if flag:
            count += 1;
    return count


if __name__ == '__main__':
    print(finalVal())

    # https://leetcode.com/problems/count-the-number-of-consistent-strings/
