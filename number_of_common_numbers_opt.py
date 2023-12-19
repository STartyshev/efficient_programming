from console_ui import *
from correct_initialization import *
from error_output import *
from pympler import tracker
import logging
import time

logger = logging.getLogger('lab18.FirstTaskOpt')


# Задача №1
def ui_number_of_common_numbers():
    """
    Функция реализующая пользовательский интерфейс в консоли для поиска кол-ва общих чисел в двух массивах.
    """
    # Два массива в которых будет осуществляться поиск общих чисел
    first_array = None
    second_array = None
    # Количество общих чисел двух массивов
    num_of_common_numbers = None
    while True:
        system('CLS')

        match main_menu_for_tasks(
            task_name='Проверка двух массивов на количество общих чисел.'
        ):
            # Условие задачи
            case 1:
                system('CLS')
                print(
                    'Входные данные: два массива с числами. Требуется проверить сколько у массивов общих чисел. '
                    'Также число будет считаться общим если оно входит в один массив, а в другом массиве находится '
                    'его перевернутая версия.'
                )
                system('PAUSE')

            # Ввод исходных данных
            case 2:
                system('CLS')
                while True:
                    match ui_menu(
                        'Способ инициализации.\n'
                        '1. Вручную.\n'
                        '2. Автоматически.'
                    ):
                        # Инициализация массивов вручную
                        case 1:
                            system('CLS')
                            print('Инициализация первого массива: ')
                            first_array = ui_array_init_opt()
                            print('Инициализация второго массива: ')
                            second_array = ui_array_init_opt()
                            break

                        # Инициализация массивов случайным образом
                        case 2:
                            system('CLS')
                            print('Инициализация первого массива: ')
                            start = tracker.SummaryTracker()
                            start_time = time.time()
                            first_array = auto_array_init_opt()
                            print('Инициализация второго массива: ')
                            second_array = auto_array_init_opt()
                            print(f"Память задействованная при инициализации двух массивов:")
                            start.print_diff()
                            end_time = time.time()
                            print(f"Время инициализации двух массивов: {end_time - start_time}\n")
                            break

                        case _:
                            print_error_message('В меню всего 2 пункта. Попробуйте еще раз.')

                print('Инициализация массивов прошла успешно.')
                system('PAUSE')

            # Выполнение алгоритма
            case 3:
                system('CLS')
                if first_array is None or second_array is None or len(first_array) < 1 or len(second_array) < 1:
                    print_error_message(
                        'Невозможно выполнить алгоритм, так как один или оба массива пустые. '
                        'Заполните массивы и попробуйте еще раз.'
                    )
                else:
                    num_of_common_numbers = number_of_common_numbers(first_array, second_array)
                    print('Алгоритм успешно выполнен!')
                    system('PAUSE')

            # Вывод результатов работы алгоритма
            case 4:
                system('CLS')
                if num_of_common_numbers is not None:
                    print(
                        f"Результат работы алгоритма.\n"
                        f"Первый массива: {' '.join(map(str, first_array))}\n"
                        f"Второй массив: {' '.join(map(str, second_array))}\n"
                        f"Количество общих чисел в обоих массивах: {num_of_common_numbers}"
                    )
                    system('PAUSE')
                else:
                    print_error_message(
                        'Невозможно вывести результат работы алгоритма, так как алгоритм не был выполнен. '
                        'Запустите работу алгоритма и попробуйте еще раз.'
                    )

            # Выход в главное меню
            case 5:
                break

            case _:
                print_error_message('В меню всего 5 пунктов. Попробуйте еще раз.')


def number_of_common_numbers(first_array, second_array):
    """
    Функция находит количество общих чисел в двух массивах.
    Также, число считается общим если оно входит в один массив, а в другом
    находится его перевернутая версия.
    :param first_array: Первый массив чисел;
    :param second_array: второй массив чисел.
    :return: Возвращает количество общих чисел двух массивов.
    """
    start = tracker.SummaryTracker()
    start_time = time.time()
    # Список в который будут добавляться общие числа
    list_of_common_numbers = []
    for direct_num, reverse_num in zip(map(str, first_array), map(lambda x: x[::-1], map(str, first_array))):
        # Если число из первого массива или его обратная версия находятся во втором массиве
        # И это число еще не обрабатывалось прежде т. е. его нет в списке общих чисел
        # То оно добавляется в список
        if ((direct_num in map(str, second_array) or reverse_num in map(str, second_array))
                and direct_num not in map(str, list_of_common_numbers)):
            list_of_common_numbers.append(direct_num)
    print(f"Память задействованная при выполнении алгоритма:")
    start.print_diff()
    end_time = time.time()
    print(f"Время выполнения алгоритма: {end_time - start_time}\n")
    return len(list_of_common_numbers)
