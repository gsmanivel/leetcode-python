def coding():
    # variable declaration - 1
    mani = sin2 = ayush = "manman-family"
    print(mani)
    print(sin2)
    print(ayush)

    # variable declaration - 2
    mani_age, sin2_age, ayush_age = 34, 34, 6
    print(mani_age)
    print(sin2_age)
    print(ayush_age)

    # type conversion
    mani_exp = '7'
    print(type(mani_exp))
    print(type(int(mani_exp)))

    # Invalid type conversion (Try it)
    # sin2_exp = '12inbank'
    # print(int(sin2_exp))

    # Hilarious
    print(type(12))
    print(type(3.7))
    print(type(True))
    print(type('hi'))

    print(int(12.0))
    print(int('12'))
    print(int(12.9))
    print(int(12.999))
    print(int(12.99999999999990899999999999))

    print(float(12))
    print(float('12'))

    print(bool('True'))
    print(bool('False'))  # Note  this

    print(bool(0))    # Only bool(0) is considered as Real boolean - False
    print(bool(1))
    print(bool(10))


if __name__ == '__main__':
    coding()
