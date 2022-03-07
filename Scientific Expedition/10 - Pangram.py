'''
Панграмма (Греческий:παν γράμμα, pan gramma, "каждая буква") или предложение состоящее из разных букв алфавита, используя каждую букву по крайней мере один раз. Возможно, вы знакомы с хорошо известными панграммами "Эй, жлоб! Где туз? Прячь юных съёмщиц в шкаф" или "Любя, съешь щипцы, — вздохнёт мэр, — кайф жгуч".

Для этого задания, вы будете использовать латинский алфавит (A-Z). У вас есть текст с латинскими буквами и знаками препинания. Вы должны проверить является ли предложение панграммой или нет. Регистр не имеет значения.

Входные данные: Текст как строка.

Выходные данные: Является предложение панграммой или нет как логическое.
'''

from string import ascii_lowercase

def check_pangram(text):
    return all(itm in text.lower() for itm in ascii_lowercase)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
    print('If it is done - it is Done. Go Check is NOW!')

