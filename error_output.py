from os import system


def print_error_message(message):
    """
    Функция реализующая форматированный вывод сообщения об ошибке в консоль.
    :param message: Текст сообщения об ошибке.
    """
    system('CLS')
    print(message)
    system('PAUSE')
    system('CLS')
