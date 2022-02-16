def finalVal():
    indices = [4, 5, 6, 7, 0, 2, 1, 3]
    s = "codeleet"

    source = list(s)
    rest = ''
    for i in range(len(source)):
        rest += source[indices.index(i)]
    return rest


if __name__ == '__main__':
    print(finalVal())

# https://leetcode.com/problems/shuffle-string/
