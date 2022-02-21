def opsDemo():
    name1 = 'mani'
    name2 = 'mani'

    # verify if both string are same
    print('name1 is name2', name1 is name2)
    print('name1 == name2', name1 == name2)

    books1 = ['java', 'python', 'ruby']
    books2 = ['java', 'python', 'ruby']

    # verify if books1 and books2 list are same
    print('books1 is books2', books1 is books2)
    print('books1 == books2', books1 == books2)

    num1 = 1
    num2 = 1

    print('num1==num2', num1 == num2)
    print('num1 is num2', num1 is num2)


if __name__ == '__main__':
    opsDemo()
