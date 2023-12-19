from console_ui import *
from correct_initialization import *
from error_output import *
import logging
from pympler import tracker
import time

logger = logging.getLogger('lab18.FirstTask')


# Задача №1
def ui_number_of_common_numbers():
    """
    Функция реализующая пользовательский интерфейс в консоли для поиска кол-ва общих чисел в двух массивах.
    """
    # Два массива в которых будет осуществляться поиск общих чисел
    first_array = []
    second_array = []
    # Количество общих чисел двух массивов
    num_of_common_numbers = None
    while True:
        system('CLS')
        main_menu_item = main_menu_for_tasks(
            task_name='Проверка двух массивов на количество общих чисел.'
        )

        match main_menu_item:
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
                first_array = []
                second_array = []
                system('CLS')
                while True:
                    initialization_item = ui_menu(
                        'Способ инициализации.\n'
                        '1. Вручную.\n'
                        '2. Автоматически.'
                    )
                    match initialization_item:
                        # Инициализация массивов вручную
                        case 1:
                            system('CLS')
                            print('Инициализация первого массива: ')
                            ui_array_init(first_array)
                            print('Инициализация второго массива: ')
                            ui_array_init(second_array)
                            print(f"Память задействованная при инициализации двух массивов:")
                            break

                        # Инициализация массивов случайным образом
                        case 2:
                            system('CLS')
                            print('Инициализация первого массива: ')
                            start = tracker.SummaryTracker()
                            start_time = time.time()
                            auto_array_init(first_array)
                            print('Инициализация второго массива: ')
                            auto_array_init(second_array)
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
                if len(first_array) < 1 or len(second_array) < 1:
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
    num_of_common_numbers = 0
    # Список в который будут добавляться общие числа
    list_of_common_numbers = []
    for elem in first_array:
        # Если число из первого массива или его обратная версия находятся во втором массиве
        # И это число еще не обрабатывалось прежде т. е. его нет в списке общих чисел
        # То оно добавляется в список и кол-во общих чисел увеличивается на 1
        if ((str(elem) in list(map(str, second_array)) or str(elem)[::-1] in list(map(str, second_array))) and
                elem not in list_of_common_numbers):
            num_of_common_numbers += 1
            list_of_common_numbers.append(elem)
    print(f"Память задействованная при выполнении алгоритма:")
    end_time = time.time()
    start.print_diff()
    print(f"Время выполнения алгоритма: {end_time - start_time}\n")
    return num_of_common_numbers
