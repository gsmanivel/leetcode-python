def finalVal():
    s = "Hello how are you Contestant"
    k = 4

    # Solution # 1
    # return " ".join(s.split(" ")[:k])

    # Solution # 2
    result = []
    str = s.split(" ")
    for i in range(0, k):
        result.append(str[i])
    return " ".join(result)


if __name__ == '__main__':
    print(finalVal())

    # https://leetcode.com/problems/truncate-sentence/
