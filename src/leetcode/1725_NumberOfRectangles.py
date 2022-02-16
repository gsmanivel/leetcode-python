def finalVal():
    rectangles = [[5, 8], [3, 9], [3, 12]]

    result = 0
    maxSide = 0
    for rectangle in rectangles:
        minNum = min(rectangle[0], rectangle[1])
        if maxSide < minNum:
            maxSide = minNum

    for rectangle in rectangles:
        if maxSide <= rectangle[0] and maxSide <= rectangle[1]:
            result += 1
    return result


if __name__ == '__main__':
    print(finalVal())

    # https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/
