'''Вам надо проверить, что 2 данные строки изометричны.
Это значит что символ из одной строки может стать в соответствие символам из другой строки.
Один символ одной строки может соответствовать только одному символу другой строки.
Два или более символа одной строки могут соответствовать одному символу другой строки, но не наоборот.'''


def isometric_strings(a, b):
    # your code here
    return len(set(zip(a, b))) == len(set(a))
    # map = {}
    # for s1, s2 in zip(a, b):
    #     if map.setdefault(s1, s2) != s2: # setdefault вернет значение по умолчанию! аргумент s2
    #         return False
    # return Trues

if __name__ == "__main__":
    print("Example:")
    print(isometric_strings("add", "egg"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert isometric_strings("add", "egg") == True
    assert isometric_strings("foo", "bar") == False
    assert isometric_strings("", "") == True
    assert isometric_strings("all", "all") == True
    assert isometric_strings("gogopy", "doodle") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
