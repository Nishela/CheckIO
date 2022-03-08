'''
Джо Палука обладает такими толстыми пальцами, что всегда задевает клавишу “Caps Lock” когда пытается нажать кнопку “a”. (Правда когда Джо пытается напечатать заглавную версию “a”, требующую нажатия нескольких клавиш, он более внимателен, и всегда жмет [Shift] + [a] правильно). Ваша программа должна вернуть то, что получится у Джо при наборе переданного текста. “Caps Lock” влияет только на кнопки от “a” до “z”, и не оказывает эффекта на другие клавиши. Перед набором текст “Caps Lock” выключен.

В клавиатуре Джо Caps Lock всегда выводит буквы в верхнем регистре. Это значит, что если Caps Lock нажат и Джо нажимает Shift + 'b', он получил 'B' (в верхнем регистре)

Входные данные: Строка. Текст, который печатает Джо.

Выходные данные: Строка. Текст, который получится у Джо после набора.
'''

def caps_lock(text: str) -> str:
    text_sp = text.split('a')
    for idx, itm in enumerate(text_sp):
        if idx & 1:
            text_sp[idx] = itm.upper()
    return ''.join(text_sp)
    # return ''.join((itm.upper() if (idx & 1) else itm for idx, itm in enumerate(text.split('a'))))



if __name__ == "__main__":
    print("Example:")
    print(caps_lock("Why are you asking me that?"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
    assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
    assert caps_lock("Aloha from Hawaii") == "Aloh FROM HwII"
    print("Coding complete? Click 'Check' to earn cool rewards!")

