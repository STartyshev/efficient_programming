import number_of_common_numbers
import number_of_common_numbers_opt
from distance_between_points import *
from arithmetic_conversion import *
from error_output import *
import logging


def main():
    """
    Функция старта главного меню.
    """
    while True:
        task_selection_item = ui_menu(
            'Меню выбора задания.\n'
            '1. Проверка двух массивов на количество общих чисел.\n'
            '2. Расстояние между точками.\n'
            '3. Логическое следствие элементов трех массивов.\n'
            '4. Выход из программы.'
        )

        logger = logging.getLogger('lab18')
        logger.setLevel(logging.DEBUG)
        sh = logging.StreamHandler()
        sh.setFormatter(logging.Formatter('-----%(asctime)s _ %(name)s:%(lineno)s _ %(levelname)s _ %(message)s'))
        sh.setLevel(logging.DEBUG)
        logger.addHandler(sh)

        match task_selection_item:
            case 1:
                opt_version = input(
                    'Хотите выбрать оптимизированную версию?\n'
                    '1. Да.\n'
                    '2. Нет.\n'
                )
                if opt_version == '2':
                    system('PAUSE')
                    number_of_common_numbers.ui_number_of_common_numbers()
                else:
                    system('PAUSE')
                    number_of_common_numbers_opt.ui_number_of_common_numbers()

            case 2:
                ui_distance_between_points()

            case 3:
                ui_arithmetic_conversion()

            case 4:
                system('CLS')
                return

            case _:
                print_error_message('В меню всего 4 пункта. Попробуйте еще раз.')


if __name__ == '__main__':
    main()
