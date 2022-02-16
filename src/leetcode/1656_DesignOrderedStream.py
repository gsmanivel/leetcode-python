from src.leetcode.OderedStream import OrderedStream


def finalVal():
    obj = OrderedStream(5)
    print(obj.insert(3, "ccccc"))
    print(obj.insert(1, "aaaaa"))
    print(obj.insert(2, "bbbbb"))
    print(obj.insert(5, "eeeee"))
    print(obj.insert(4, "ddddd"))


if __name__ == '__main__':
    print(finalVal())

    # https://leetcode.com/problems/design-an-ordered-stream/
