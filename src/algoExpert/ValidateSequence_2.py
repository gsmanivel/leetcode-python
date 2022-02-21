def coding():
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [22, 25, 6]

    seqIndex = 0
    for arrayNum in array:
        if seqIndex == len(sequence):
            break
        if sequence[seqIndex] == arrayNum:
            seqIndex += 1
    return seqIndex == len(sequence)


def coding2():
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [22, 25, 6]

    seqIndex = 0
    arrIndex = 0
    while seqIndex < len(sequence) and arrIndex < len(array):
        if sequence[seqIndex] == array[arrIndex]:
            seqIndex += 1
        arrIndex += 1
    return seqIndex == len(sequence)


if __name__ == "__main__":
    print(coding2())
