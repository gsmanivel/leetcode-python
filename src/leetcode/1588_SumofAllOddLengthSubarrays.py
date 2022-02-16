def finalVal():
    arr = [10, 11, 12]

    result = 0
    arrLen = len(arr)
    oddNumArr = []
    for i in range(2, len(arr) + 1):
        if i % 2 != 0:
            oddNumArr.append(i)

    for oddNumLoop in range(len(oddNumArr)):
        for preFinalLoop in range(0, arrLen):
            oddNum = oddNumArr[oddNumLoop]
            if (preFinalLoop + oddNum) - 1 < arrLen:
                for finalLoop in range(0, oddNum):
                    result = result + arr[preFinalLoop + finalLoop]
            else:
                break
    return result + sum(arr)


if __name__ == '__main__':
    print(finalVal())

    # https: // leetcode.com / problems / sum - of - all - odd - length - subarrays /
