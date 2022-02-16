def finalVal():
    image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]

    result = []
    for innerImage in image:
        newInnerImage = []
        innerImage.reverse()
        for i in range(0, len(innerImage)):
            newInnerImage.append(0) if innerImage[i] == 1 else newInnerImage.append(1)
        result.append(newInnerImage)
    return result


if __name__ == '__main__':
    print(finalVal())

    # https://leetcode.com/problems/flipping-an-image/
