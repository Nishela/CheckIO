'''
Когда-нибудь пробовали отправить секретное сообщение кому-то не пользуясь услугами почты? Вы можете использовать газету, чтобы рассказать кому-то свой секрет. Даже если кто-то найдет ваше сообщение, легко отмахнуться и сказать что это паранойя и теория заговора. Один из самых простых способов спрятать ваше секретное сообщение это использовать заглавные буквы. Давайте найдем несколько таких секретных сообщений.

Дан кусок текста. Соберите все заглавные буквы в одно слово в том порядке как они встречаются в куске текста.

Например: текст = " H ow are you? E h, ok. L ow or L ower? O hhh.", если мы соберем все заглавные буквы, то получим сообщение "HELLO".

Входные данные: Текст как строка (юникод).

Выходные данные: Секретное сообщение как строка или пустая строка.

'''

def find_message(message: str) -> str:
    return ''.join(itm for itm in message if itm.isupper())



if __name__ == '__main__':
    print("Example:")
    print(find_message(('How are you? Eh, ok. Low or Lower? '
 + 'Ohhh.')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert find_message(('How are you? Eh, ok. Low or Lower? '
 + 'Ohhh.')) == 'HELLO'
    assert find_message('hello world!') == ''
    assert find_message('HELLO WORLD!!!') == 'HELLOWORLD'
    print("Coding complete? Click 'Check' to earn cool rewards!")

