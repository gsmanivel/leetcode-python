def finalVal():
    encoded = [1,2,3]
    first = 1
    # Result = [4,2,0,7,4]

    rest = [first]
    for i in encoded:
        xor = i ^ first
        rest.append(xor)
        first = xor
    return rest


if __name__ == '__main__':
    print(finalVal())

#  https://leetcode.com/problems/decode-xored-array/
