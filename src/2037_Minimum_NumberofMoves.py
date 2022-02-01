def finalVal():
    seats = [3, 1, 5]
    students = [2, 7, 4]

    result = 0
    seats.sort()
    students.sort()

    for i in range(len(seats)):
        result += abs(seats[i]-students[i])
    return result


if __name__ == '__main__':
    print(finalVal())

# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/
