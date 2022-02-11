def finalVal():
    points = [[1, 1], [3, 4], [-1, 0]]
    result = 0
    for i in range(0, len(points)-1):
        diff1 = abs(points[i][0] - points[i+1][0])
        diff2 = abs(points[i][1] - points[i + 1][1])
        result += max(diff1, diff2)
    return result


if __name__ == '__main__':
    print(finalVal())

    # https://leetcode.com/problems/minimum-time-visiting-all-points/
