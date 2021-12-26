'''У вас есть текст и список слов. Вам нужно проверить, появляются ли слова в списке в том же порядке, что и в данном тексте.

Случаев, которых следует ожидать при решении этой задачи:

слова из списка нет в тексте - ваша функция должна вернуть False;
любое слово может встречаться в тексте более одного раза - используйте только первое;
два слова в данном списке совпадают - ваша функция должна возвращать False;
условие чувствительно к регистру, что означает, что «привет» и «привет» - два разных слова;
текст состоит только из английских букв и пробелов.
Вход: два аргумента. Первый - заданный текст, второй - список слов.

Вывод: bool.'''

def words_order(text: str, words: list) -> bool:
    # your code here
    result = []
    for word in text.split():
        if word in words and word not in result:
            result.append(word)
    return True if ''.join(result) == ''.join(words) else False



if __name__ == '__main__':
    print("Example:")
    print(words_order('hi world im here', ['world', 'here']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert words_order('hi world im here', ['world', 'here']) == True
    assert words_order('hi world im here', ['here', 'world']) == False
    assert words_order('hi world im here', ['world']) == True
    assert words_order('hi world im here',
 ['world', 'here', 'hi']) == False
    assert words_order('hi world im here',
 ['world', 'im', 'here']) == True
    assert words_order('hi world im here',
 ['world', 'hi', 'here']) == False
    assert words_order('hi world im here', ['world', 'world']) == False
    assert words_order('hi world im here',
 ['country', 'world']) == False
    assert words_order('hi world im here', ['wo', 'rld']) == False
    assert words_order('', ['world', 'here']) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")

