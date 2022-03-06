'''
Бывают ситуации, когда среди огромного количества файлов на вашем компьютере или в отдельной папке вам необходимо найти файлы определенного типа - например, изображения с расширением '.jpg' или документы с расширением '.txt' или файлы, в названии которых есть слово 'butterfly'. Делая это вручную можно потратить слишком много времени. Именно для облегчения подобных задач служит матчинг или паттерны для поиска файлов по определенной маске.
Эта миссия поможет вам разобраться с тем, как это работает.

Ваша задача - определить, соответствует ли заданное имя файла заданному поисковому паттерну.
'''


def unix_match(filename: str, pattern: str) -> bool:
    import re
    pattern = pattern.replace('.', '\.').replace('*', '.*').replace('?', '.')
    res = re.match(pattern, filename)
    return filename == res[0] if res else False


if __name__ == '__main__':
    print("Example:")
    print(unix_match('somefile.txt', '*'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match('somefile.txt', '*') == True
    assert unix_match('other.exe', '*') == True
    assert unix_match('my.exe', '*.txt') == False
    assert unix_match('log1.txt', 'log?.txt') == True
    assert unix_match('log12.txt', 'log?.txt') == False
    assert unix_match('log12.txt', 'log??.txt') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
