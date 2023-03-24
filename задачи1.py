# функции
def array_print(array):  # задача 1 - вывод 1, 3, 2 с конца элемента массива
    print('Исходный массив: ', array)
    try:
        return 'Первый, третий, второй с конца элементы: {0}, {1}, {2}'.format(array[0], array[2], array[-2])
    except IndexError:
        return 'Массив слишком мал!'


def exponent(array, exp):  # задача 2 - возведение N элемента в N степень в массиве
    print('Исходный массив: ', array)
    print('Возведение элемента с индексом {0} в степень {0}'.format(exp))
    try:
        array[exp] = pow(array[exp], exp)
    except IndexError:
        print('Элемента с таким индексом не существует!')
        return -1
    else:
        return array


def index_search(string, symbol):  # задача 3 - вывод индекса второго символа в строке
    print('Поиск индекса второго символа "{0}" в строке "{1}"'.format(symbol, string))
    indexes = [i for i, s in enumerate(string) if s == symbol]
    try:
        return 'Индекс второго символа: {0}'.format(indexes[1])
    except IndexError:
        if len(indexes) == 0:
            return 'Cимвол не найден!'
        else:
            return 'Второй индекс не найден!'


def count_zeroes(number):  # задача 4 - вывод положения второго индекса заданного символа в строке
    print('Подсчет нулей в конце числа ', number)
    number = str(number)
    number = number[::-1]
    count = 0
    for n in number:
        if n == '0':
            count += 1
        else:
            break
    return 'Нулей в конце числа: {0} '.format(count)


def reverse_string(string):  # задача 5 - переворот строки
    print('Переворот строки "{0}"'.format(string))
    string = string[::-1]
    return 'Результат: {0}'.format(string)


def same_letters(string):  # задача 6 - проверка массива на одинаковость элементов
    print('Проверка массива {0} на одинаковые значения элементов'.format(string))
    if len(string) == 1 or len(string) == 0:
        return 'Недостаточно элементов'
    check = 'Не все значения одинаковы'
    for i in range(0, len(string) - 1):
        if string[i] == string[i + 1]:
            check = 'Все значения одинаковы'
        else:
            check = 'Не все значения одинаковы'
            break
    return check


def password_check(password):  # задача 7 - проверка пароля
    print('Проверка безопасности пароля ', password)
    if len(password) < 16:
        return ' ! Длина пароля должна быть не меньше 16 ! '
    elif not password.isalnum():
        return ' ! Пароль не должен содержать символы ! '
    else:
        check_Upper, check_Lower, check_Number, check_Letter = False, False, False, False
        for symbol in password:
            if symbol == symbol.upper():  # если символ - заглавная буква
                check_Upper = True
            if symbol == symbol.lower():  # если символ - строчная буква
                check_Lower = True
            if symbol.isdigit():  # если символ - цифра
                check_Number = True
            if symbol.isalpha():  # если символ - буква (нужно для тех случаев, когда все символы - цифра)
                check_Letter = True
        if not check_Letter:
            return ' ! Пароль должен содержать хотя бы одну букву ! '
        elif not check_Lower:
            return ' ! Пароль должен содержать хотя бы одну строчную букву ! '
        elif not check_Upper:
            return ' ! Пароль должен содержать хотя бы одну заглавную букву ! '
        elif not check_Number:
            return ' ! Пароль должен содержать хотя бы одну цифру ! '
        else:
            return 'Все ок!'


def flatten(ls):  # задача 8 - превращение многомерного массива в одномерный
    flat_list = []  # массив, в который будут добавляться все элементы
    for item in ls:
        if isinstance(item, list) or isinstance(item, tuple):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list


def max_key(dic):  # задача 9 - вывод ключа максимального значения в словаре
    print('Словарь: ', dic)
    return 'Ключ максимального значения в словаре: {0}'.format(max(dic, key=dic.get))


def same_values(array):  # задача 10 - вывод неуникальных элементов в массиве
    print('Исходный список: ', array)
    same_array = []
    check = False
    for item1 in range(len(array)):
        for item2 in range(len(array)):
            if item1 != item2:
                if array[item1] == array[item2]:
                    check = True
                    break
                else:
                    check = False
        if check:
            same_array.append(array[item1])
    return 'Неуникальные значения: {0}'.format(same_array)


# основной код

# задача 1 - вывод 1, 3, 2 с конца элемента массива
print('\n--Задача 1--\n')
print(array_print([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(array_print([1]))

# задача 2 - возведение N элемента в N степень в массиве
print('\n--Задача 2--\n')
print(exponent([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
print(exponent([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14))

# задача 3 - вывод индекса второго символа в строке
print('\n--Задача 3--\n')
print(index_search('Карамель', 'а'))
print(index_search('Карамель', 'м'))
print(index_search('Карамель', 'у'))

# задача 4 - вывод положения второго индекса заданного символа в строке
print('\n--Задача 4--\n')
print(count_zeroes('1001000000'))
print(count_zeroes('01001'))

# задача 5 - переворот строки
print('\n--Задача 5--\n')
print(reverse_string('бордалвглагор'))

# задача 6 - проверка массива на одинаковость элементов
print('\n--Задача 6--\n')
print(same_letters([]))
print(same_letters([0]))
print(same_letters([0, 0, 0, 0]))
print(same_letters([0, 0, 0, 1, 0]))
print(same_letters([0, 0, 0, 0, 1]))

# задача 7 - проверка пароля
print('\n--Задача 7--\n')
print(password_check('*23'))
print(password_check('*23343343923232323'))
print(password_check('2344388209342393479'))
print(password_check('FDSDIFIDISIIDFIDIIFDF'))
print(password_check('sdsidhishdsihdhihsd'))
print(password_check('sdsidhiDDDshdsiDDhdhihsd'))
print(password_check('SDD14ssdsojdojAAAAAAAAAA'))

# задача 8 - превращение многомерного массива в одномерный
print('\n--Задача 8--\n')
a = [0, [1, 2, 3], [[4, 5], (6, 7), [8, 9, (10, 11)]], 12, ()]
print('Сложный список: ', a)
print('Вытянутый список: ', flatten(a))
b = ['2', [3, 4], [5, ('2', '!')]]
print('Сложный список: ', b)
print('Вытянутый список: ', flatten(b))

# задача 9 - вывод ключа максимального значения в словаре
print('\n--Задача 9--\n')
print(max_key({'a': 1.0, 'b': 20.0, 'c': 0.3, 'd': -40.5}))

# задача 10 - вывод неуникальных элементов в массиве
print('\n--Задача 10--\n')
print(same_values([1, 2, 2, 3, 4, 5, 6, 5, 7, 8, 3, 9]))
print(same_values([1, 2, 3]))
