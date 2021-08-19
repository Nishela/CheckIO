'''В комьютерной науке и дискретной математике, инверсия - это пара позиций последовательности,
где элементы на этих позициях выпадают из естественного порядка.
Таким образом, если мы используем порядок по возрастанию для группы чисел, то инверсия получается,
когда более крупные цифры стоят перед меньшим значением в последовательности.
Проверим такой пример последовательности: (1, 2, 5, 3, 4, 7, 6) и мы можем видеть здесь три инверсии
- 5 и 3;
- 5 и 4;
- 7 и 6.
Вам дана последовательность уникальных чисел и вы должны подсчитать число инверсий в этой последовательности.
Входные данные: Последовательность как кортеж целых чисел.
Выходные данные: Количество инверсий.'''


def count_inversion(sequence: list) -> int:
    """
        Count inversions in a sequence of numbers
    """
    count = 0
    for idx_m in range(0, len(sequence)):
        for idx in range(idx_m + 1, len(sequence)):
            if sequence[idx_m] > sequence[idx]:
                count += 1
    return count


if __name__ == '__main__':
    print("Example:");
    print(count_inversion([1, 2, 5, 3, 4, 7, 6]));

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

