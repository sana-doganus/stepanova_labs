from collections import Counter


def transpose(mat):  # задача 1 - транспонирование
    # [list(i) for i in zip(*mat)]
    return list(zip(*mat))
    # *mat - все элементы матрицы, аналогично выражению mat[0], mat[1], ..., mat[n]
    # функция zip берет все элементы матрицы и сопоставляет их содержимое по номерам внутренних элементов,
    # создавая массив из кортежей (zip-object). list(zip()) превращает zip-object в список


def matrix_print(mat):  # печать матрицы
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print('\t{:<5}'.format(mat[i][j]), end='')  # форматирование по левому краю с табуляцией и 5 пробелами
        print()


def task1(mat):  # оформление 1 задачи
    print('\tМатрица: \n')
    if not mat:
        print('\t!Нечего транспонировать!')
    else:
        matrix_print(mat)
        print('\n\tТранспонированная матрица: \n')
        matrix_print(transpose(mat))
        print('\n')


def assign_pets(lst):  # задача 2 - оптимизация хранения данных о владельцах и животных
    pets_dict = {}
    # owner - строка с именем и фамилией, pets = строка с именем питомца и возрастом
    # проходим по входному списку: владельцев добавляем в ключи словаря, питомцев - в значения
    for tup in lst:
        owner = '{0} {1}'.format(tup[2], tup[3])
        pets = '{0}, возраст - {1}'.format(tup[0], tup[1])
        # pets_dict.setdefault(owner, list()).append(pets)
        if owner not in pets_dict:
            pets_dict.setdefault(owner, pets)
        else:
            pets_dict.update({owner: pets_dict.get(owner) + '; ' + pets})
    return pets_dict


def task2(lst):  # оформление 2 задачи
    print('\tИсходные данные:', end=' ')
    if not lst:
        print('Пустой массив!\n')
        return None
    print()
    for elem in lst:
        print('\t', elem)
    print('\n\tПосле оптимизации:', end=' ')
    for tup in lst:
        if len(tup) != 4:
            print('Что-то не так с кортежами!\n')
            return None
    print()
    for key in assign_pets(lst):
        print('\t', key, ': ', assign_pets(lst).get(key), sep='')
    print('\n')


def rarest_word(string):  # задача 3 - самое редкое слово
    if not string or string.isdigit():
        return 'Слов нет'
    # чистка строки от цифр и знаков препинания, перевод в нижний регистр
    new_string = ''
    for i in string:
        if i.isalpha() or i.isspace():
            new_string = new_string + i.lower()

    # разбивка получившейся строки на слова
    split_string = new_string.split()

    # создание словаря с ключами-словами и значениями-колвом появлений в строке
    word_freqs = Counter(split_string)

    if not word_freqs:  # прекращение функцию при пустом словаре чтобы прога не ломалась
        return 'Слов нет'

    # генератор списка из слов с наименьшим появлением
    words = [i for i in word_freqs if word_freqs.get(i) == min(word_freqs.values())]

    # возврат первого значения в списке, отсортированном по алфавиту
    return sorted(words)[0]


def task3(string):  # оформление 3 задачи
    print('\tСтрока: ', string)
    print('\tСамое редкое слово: ', rarest_word(string), '\n')


def most_frequent_word(string):  # задача 4 - самая частая буква
    if not string or string.isdigit():
        return 'Букв нет'
    # чистка строки от небуквенных символов, перевод в нижний регистр
    new_string = ''.join(filter(str.isalpha, string.lower()))

    # создание словаря с ключами-буквами и значениями-колвом появлений в строке
    letters = Counter(new_string)

    if not letters:
        return 'Букв нет'

    # максимальное значение словаря
    max_value = max(letters.values())

    # список букв с максимальным колвом появлений
    max_letters = [i for i in letters if letters[i] == max_value]

    # возврат первого значения в списке, отсортированном по алфавиту
    return sorted(max_letters)[0]


def task4(string):  # оформление 4 задачи
    print('\tСтрока: ', string)
    print('\tСамая частая буква: ', most_frequent_word(string), '\n')


def palindrome(string):  # задача 5 - определение палиндромности
    # убираем пробелы
    string = string.replace(' ', '')

    # 1) если строка <= 1, то она автоматически считается палиндромом
    # 2) если строка больше нуля, то палиндромим ее до тех пор, пока крайние элементы не совпадут и выпадет False,
    # или пока строка не станет равной 1

    result = True
    if len(string) > 1:
        if string[0].lower() == string[-1].lower():
            result = palindrome(string[1:-1])
        else:
            result = False
    return result


def task5(string):  # оформление 5 задачи
    print('\t', string, end=' - ')
    print('палиндром') if palindrome(string) else print('НЕ палиндром')


def freq_sort(array):  # задача 6 - сортировка по частоте элементов + порядку появления при одинаковой частоте
    # словарь, где ключи - цифры, значения - их частота
    nums = Counter(array)

    # переворот словаря задом-наперед. теперь ключ - частота появления цифр, значение - список цифр
    inverse_nums = {}
    for key, value in nums.items():
        inverse_nums.setdefault(value, list()).append(key)

    # сортировка ключей в словаре, чтобы они были по возрастанию (1:[], 2:[], 3:[] и т.д)
    sorted_nums = dict(sorted(inverse_nums.items()))

    # проход по значениям и вынос в конечный список (элементы повторяются столько раз, сколько указано в ключе)
    result = []
    for key, value in sorted_nums.items():
        for numbers in value:
            result.extend([numbers for i in range(key)])
    return result


def task6(array):  # оформление 6 задачи
    print('\tИсходный список: ', array)
    print('\tСортировка по частоте: ', freq_sort(array), '\n')


def three_conseq_words(string):  # задача 7 - проверка непрерывной последовательности из трех слов.
    array = string.split()
    count = 0
    for i in range(len(array)):
        count += 1
        if not array[i].isalpha():
            count = 0
        if count == 3:
            return True
    return False


def task7(string):  # оформление 7 задачи
    print('\t', string, end=' - ')
    print('Да') if three_conseq_words(string) else print('Нет')


def max_consequence(string):  # задача 8 - максимальная длина непрерывной последовательности одинаковых букв
    string = string.lower()
    count = 1
    save = 0
    for i in range(len(string) - 1):
        if string[i] == string[i + 1] and string[i].isalpha():
            count += 1
            save = count if save < count else save
        else:
            count = 1
    return save


def task8(string):  # оформление 8 задачи
    print('\tВ строке "{0}" максимум {1} идущих подряд одинаковых букв'.format(string, max_consequence(string)))


def math_expression(string):  # 9 - вычисление арифметического выражения в строке
    try:
        return eval(string)
    except Exception as error:
        return error


def task9(string):  # оформление 9 задачи
    print('\t', string, ' = ', math_expression(string))


def summed_dict(list_of_dicts):  # задача 10 - новый словарь
    new_dict = {}

    # проход по каждому ключу в словарях
    for dic in list_of_dicts:
        for key in dic.keys():
            # если ключа нет в новом словаре, добавляем его
            if key not in new_dict.keys():
                new_dict.setdefault(key, dic.get(key))
            # если ключ в словаре - обновляем его значение (складываем уже существующее с новым)
            else:
                new_dict.update({key: new_dict.get(key) + dic.get(key)})
    return new_dict


def task10(lst):  # оформление 10 задачи
    print('\tИсходные словари:', *lst, sep='\n\t')
    print('\tНовый словарь: ', summed_dict(lst), '\n')


# основной код
# задача 1
print('\n-- Задача 1. Транспонирование матрицы --\n')

task1([[0, 1, 2, 3, 4],
       [0, 1, 2, 3, 4],
       [0, 1, 2, 3, 4]])

task1([[0, 1, 2, 3, 4],
       [0, 1, 2, 3],  # код полностью выкидывает столбец с недостающим значением
       [0, 1, 2, 3, 4]])

task1([[1], [2], [3]])
task1([[1]])
task1([])


# задача 2
print('\n-- Задача 2. Оптимизация хранения данных --\n')
task2([('Дог', 10, 'Наташа', 'Романова'),
       ('Кот', 5, 'Иван', 'Иванов'),
       ('Попуг', 2, 'Наташа', 'Романова')])
task2([('Дог', 10, 'Иван', 'Ивановна'),
       ('Кот', 5, 'Лол', 'Лолыч'),
       ('Попуг', 2, 'Наташа')])
task2([('Попуг', 2, 'Наташа', 'Романова')])
task2([])


# задача 3
print('\n-- Задача 3. Самое редкое слово --\n')
task3('Пошёл в Пятерочку за хлебом и упал в яму')
task3('Аа Ааа Ау')
task3('хе хе хе!!!!!')
task3('0123')
task3('')


# задача 4
print('\n-- Задача 4. Самая частая буква --\n')
task4('Пошёл в Пятерочку за хлебом и упал в яму')
task4('Аа Ааа Ау')
task4('хе хе хе!!!!!')
task4('0123')
task4('')


# задача 5
print('\n-- Задача 5. Палиндром или нет? --\n')
task5('А роза упала на лапу Азора')
task5('кек')
task5('кекк')
task5('а')
task5('')

# задача 6
print('\n-- Задача 6. Сортировка чисел по частоте --\n')
task6([1, 9, 0, 9, 0, 1])
task6([1, 2, 3, 4, 3, 5, 5, 6, 5, 6])
task6([])

# задача 7
print('\n-- Задача 7. Наличие непрерывной последовательности из 3 слов в строке --\n')
task7('Зачем идти на 1 пару в восемь утра?')
task7('Я арбуз - а я... ананас!')
task7('12345')
task7('')

# задача 8
print('\n-- Задача 8. Максимальная длина непрерывной последовательности из одинаковых букв --\n')
task8('Ааарбуз')
task8('Ааааадвокааат')
task8('Мороженое')
task8('12345')
task8('')

# задача 9
print('\n-- Задача 9. Вычисление математического выражения --\n')
task9('2+2*2')
task9('2')
task9('2/0')
task9('2-1=')
task9('!#@')
task9('')

# задача 10
print('\n-- Задача 10. Словарь с суммами значений из других словарей --\n')

task10([{'1': 1, '2': 2},
        {'1': 1, '2': 2, '3': 3},
        {'1': 1, '2': 2, '3': 3, '4': 4},
        {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5}])

task10([{'1': 1, '2': 2, '3': 3}])
task10([])
