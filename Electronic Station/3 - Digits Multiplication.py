'''Дано положительное целое число. Вам необходимо подсчитать произведение всех цифр в этом числе,
за исключением нулей.
Для примера: Дано число 123405. Результат будет: 1*2*3*4*5=120 (не забудьте исключить нули).
Входные данные: Положительное целое число.
Выходные данные: Произведение цифр как целочисленное (int).'''

from functools import reduce
def checkio(number: int) -> int:
    new_number = str(number).replace('0', '')
    if len(new_number) > 1:
        return reduce(lambda x, y: int(x) * int(y), list(new_number))
    else:
        return int(new_number)

    # result = reduce(lambda x, y: int(x) * int(y), list(new_number)) if len(new_number) > 1 else int(new_number)

    #     if len(new_number) > 1:
    #         result = int(new_number[0]) * int(new_number[1])
    #         for itm in range(2, len(new_number)):
    #             result = result * int(new_number[itm])
    #     else:
    #         result = int(new_number[0])
    #     return result


if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

