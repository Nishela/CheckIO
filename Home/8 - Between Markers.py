'''Вам дана строка и два маркера (начальный и конечный). Вам необходимо найти текст, заключенный между двумя этими маркерами. Но есть несколько важных условий:
Начальный и конечный маркеры всегда разные
Если нет начального маркера, то началом считать начало строки
Если нет конечного маркера, то концом считать конец строки
Если нет ни конечного, ни начального маркеров, то просто вернуть всю строку
Если конечный маркер стоит перед начальным, то вернуть пустую строку
Input: Три аргумента. Все строки. Второй и третий аргументы это начальный и конечный маркеры.
Output: Строка.
Предусловия: не может быть более одного маркера одного типа'''

def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    import re

    try:
        if ('[' or ']') in begin:
            begin = f'\\{begin}'
        start = re.search(begin, text).end()
    except:
        start = 0
    try:
        if ('[' or ']') in end:
            end = f'\\{end}'
        finish = re.search(end, text).start()
    except:
        finish = None
    return text[start:finish]


if __name__ == '__main__':
    # print('Example:')
    # print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    # assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    # assert between_markers("<head><title>My new site</title></head>",
    #                        "<title>", "</title>") == "My new site", "HTML"
    # assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    # assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    # assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    # assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    assert between_markers("Never send a human to do a machine's job.", 'Never', 'do') == ' send a human to '
    print('Wow, you are doing pretty good. Time to check it!')

