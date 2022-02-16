
class OrderedStream(object):

    def __init__(self, n):
        self.input = [None] * n
        self.pointer = 0

    def insert(self, idKey, value):
        self.input[idKey - 1] = value
        ans = []
        while self.pointer < len(self.input) and self.input[self.pointer]:
            ans.append(self.input[self.pointer])
            self.pointer += 1
        return ans