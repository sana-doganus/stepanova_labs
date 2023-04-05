import re
import random


# функции
def fibonacci(num):  # задача 1 - вычисление n-ного элемента фибоначчи через рекурсию
    if num < 0 or type(num) != int:  # проверка, является ли num натуральным числом
        return 'Такого не может быть...'
    if num > 40:
        return 'Очень большое число, буду долго считать:('  # при num > 40 ответа придется ждать более одной минуты
    if num == 1 or num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)  # по формуле F = F(n-1) + F(n-2)


def task1(num):  # функция для оформления 1 задачи
    print('\t{0}-й элемент в последовательности Фибоначчи: '.format(num), end='')
    print(fibonacci(num))


def delete_same_numbers(arr1, arr2):  # задача 2 - удаление из 2 списков совпадающих элементов
    for i in arr1[:]:  # [:] делает копию 1-го списка (если юзать оригинальный, то будет проблема с индексами)
        for j in arr2:
            if i == j:
                arr1.remove(i)
                arr2.remove(j)
    return [arr1, arr2]


def task2(arr1, arr2):  # функция для оформления 2 задачи
    print('\tИзначальные списки: ', arr1, ',', arr2)
    print('\tПосле удаления одинаковых элементов: ', end='')
    print(delete_same_numbers(arr1, arr2)[0], delete_same_numbers(arr1, arr2)[1], sep=', ')


def delete_repeat(arr, num):  # задача 3 - извлечь из списка все элементы, которые встречаются не реже n раз
    count = 0  # счетчик повторяющихся элементов
    result = []
    for i in range(len(arr)):  # сравнение каждого элемента с последующими
        for j in range(i, len(arr)):
            if arr[i] == arr[j]:  # увеличение счетчика при совпадении
                count += 1
        if count >= num:  # если элемент встретился ровно или больше num раз, то в result добавляем элемент
            result.append(arr[i])
        count = 0
    result = list(set(result))  # удаление всех одинаковых элементов из result
    # если элемент один в списке, возвращает чисто его, иначе возвращает список
    return result[0] if len(result) == 1 else result


def task3(arr, num):  # функция для оформления 3 задачи
    print('\tЭлемент(ы) списка {0}, повторяющиеся не реже {1} раз: '.format(arr, num), end=' ')
    print(delete_repeat(arr, num))


def nestsum(lst):  # задача 4 - замена всех вложенных списков суммой их элементов
    nest_list = []
    for item in lst:  # проходим по списку
        # если элемент список или кортеж, то вытягиваем его и суммируем, иначе просто добавляем в конечный массив
        if isinstance(item, list) or isinstance(item, tuple):
            nest_list.append(sum(flatten(item)))
        else:
            nest_list.append(item)
    return nest_list


def flatten(lst):  # доп функция вытягивания (из прошлой лабы) для задачи 4
    flat_list = []
    for item in lst:
        if isinstance(item, list) or isinstance(item, tuple):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list


def task4(lst):  # функция для оформления 4 задачи
    print('\tИсходный список: ', lst)
    print('\tПосле замены: ', nestsum(lst))


def sequence(lst):  # задача 5 - наибольшая возрастающая подпоследовательность
    if len(lst) == 1:
        return lst
    temp, save = [], []  # списки для сохранения
    for i in range(len(lst) - 1):
        # проверка, является ли следующий элемент больше или равен предыдущему
        if lst[i + 1] >= lst[i]:
            # заносим первый элемент в temp, когда он пуст; если заносить оба элемента всегда, они будут дублироваться
            temp.append(lst[i]) if temp == [] else temp
            # заносим второй элемент в temp
            temp.append(lst[i + 1])
            if len(save) <= len(temp):  # если сохраненная последовательность меньше временной, то записываем в нее temp
                save = temp
        else:
            temp = []
    return save


def task5(lst):  # функция для оформления 5 задачи
    print('\tИсходный список:', lst)
    print('\tНаибольшая ВП: ', sequence(lst))


def zabor(text):  # задача 6 - текст зАбОрЧиКоМ
    new_text = ''
    for i in range(len(text)):
        if i % 2 == 0:
            new_text += text[i].upper()
        else:
            new_text += text[i].lower()
    return new_text


def task6(text):  # функция для оформления 6 задачи
    print('\t', text, ' --> ', zabor(text), sep='')


def rhomb(height, width):  # задача 7 - ромб по заданной ширине и высоте (самая сложная для меня задача...)
    char = random.choice('+#*')  # рандомно выбирается, какой символ печатать

    med = width // 2 + 1  # середина строки
    half = height // 2 + 1  # половина ромба (верхняя или нижняя)

    shift = 0  # сдвиг позиции элемента

    if width > height:  # шаг ширины
        # если ширина больше высоты, элементы будут сдвигаться на целое частное width+1 и height
        shift_hor = (width+1) // height
    else:  # иначе элементы сдвигаются на один шаг
        shift_hor = 1

    if height > width:  # определяет, худой ромб или нет (т.е. ромб, у которого высота больше ширины)
        shift_ver = 1
    else:
        shift_ver = 0

    # циклы печатают таблицу из символов и пробелов
    for i in range(1, height + 1):
        print('\t', end='')
        for j in range(1, width + 1):
            if i % 2 == 0 and shift_ver == 1 and i != half:  # несредние четные строки в худых ромбах будут пустыми
                print(' ', end='')
            else:
                # заполнение символами, начиная с середины и сдвигая позицию в обе стороны
                if j == (med + shift) or j == (med - shift):
                    print(char, end='')
                else:
                    print(' ', end='')
        print()  # переход на новую строку
        # далее определяется, в какой половине ромба мы находимся
        # если в верхней, то сдвиг позиции будет увеличиваться, иначе - уменьшаться (на шаг ширины)
        # в несредних четных строках худого ромба пропускается увеличение/уменьшение сдвига
        if i < half:
            if i % 2 != 0 or shift_ver == 0 or i == half:
                shift += shift_hor
        else:
            if i % 2 != 0 or shift_ver == 0 or i == half:
                shift -= shift_hor
    print()


def task7(height, width):  # оформление 7 задачи (господи помилуй как это страшно выглядит)
    print('\tВысота = {0}, ширина = {1}'.format(height, width))
    warning = ''
    # блок проверки высоты и ширины, замена на допустимые значения
    if height < 3:
        warning += 'Недостаточная высота! '
        height = 3
    if width < 3:
        warning += 'Недостаточная ширина! '
        width = 3
    if height % 2 == 0:
        warning += 'Четная высота! '
        height += 1
    if width % 2 == 0:
        warning += 'Четная ширина! '
        width += 1
    if height // width >= 2:
        warning += 'Слишком худой ромб! '
        height = width*2 - 1
    # печать предупреждений и новых значений
    if warning != '':
        print('\t{0}Наиболее близкий вариант: высота = {1}, ширина = {2}'.format(warning, height, width))
    print()
    rhomb(height, width)  # наконец-то вывод ромба


def matrix(num):  # задача 8 - квадратная матрица из сумм элементов соседей
    mat = [[0 for i in range(num)] for j in range(num)]  # генерация двумерного нулевого массива
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if i == 0 or j == 0:  # если первый ряд или строка, элемент равен единице
                mat[i][j] = 1
            else:  # иначе равен сумме элемента выше и элемента слева
                mat[i][j] = mat[i - 1][j] + mat[i][j - 1]
    return mat


def matrix_print(num):  # печать матрицы
    mat = matrix(num)
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print('\t{:<10}'.format(mat[i][j]), end='')  # форматирование по левому краю с табуляцией и 10 пробелами
        print()


def task8(num):  # функция для оформления 8 задачи
    print('\tТаблица размерностью {0}:'.format(num), '\n')
    matrix_print(num)
    print()


def string_sum_int(text):  # задача 9 - сумма чисел в строке через int
    temp = '0'
    save = 0
    for char in text:
        if char.isdigit():
            temp += char  # записывает цифры, пока не дойдет до конца числа в строке
        else:
            save += int(temp)  # преобразование строки из temp в число и сохранение в save
            temp = '0'  # 'обнуление' temp
    save = save + int(temp)  # прибавление int(temp) для правильного подсчета чисел в конце строки
    return save


def task9(text):  # функция для оформления 9 задачи
    print('\t', text, ' --> ', string_sum_int(text))


def string_sum_map(text):  # задача 10 - сумма чисел в строке через map
    temp = []
    result = []
    keys, values = range(48, 58), range(0, 10)
    nums = dict(zip(keys, values))  # словарь, где ключ - номер в юникоде, а значение - соответствующее ему число

    for i in re.findall('\d+', text):  # проход по списку из всех чисел в строке
        for j in i:
            # если символ элемента есть в словаре, то добавляем в temp значение по ключу
            if ord(j) in nums:
                temp.append(nums[ord(j)])
        temp = sum(10 ** i[0] * i[1] for i in enumerate(reversed(temp)))  # превращение цифр из temp в полные числа 
        result.append(temp)  # добавляем число в конечный массив
        temp = []
    return sum(result)


def task10(text):  # функция для оформления 10 задачи
    print('\t', text, ' --> ', string_sum_map(text))


# основной код

# задача 1
print('\n-- Задача 1. Вывод n-ного элемента последовательности Фибоначчи --\n')
task1(6)
task1(20)
task1(-1)
task1(45)

# задача 2
print('\n-- Задача 2. Удаление элементов, которые есть в обоих списках --\n')
task2([1, 2, 3, 4, 5, 6], [4, 5, 6, 7, 8, 9])
task2([1], [1])
task2([], [])

# задача 3
print('\n-- Задача 3. Извлечение из списка элементов, встречающихся не реже n раз --\n')
task3([1, 2, 3, 5, 3, 5, 3, 5], 3)
task3([1, 2, 3, 3, 3, 3], 8)
task3([1, 2, 3, 3, 3, 3], 0)
task3([], 0)
task3(['d', 'd', 'd', 1, 1, 1], 3)

# задача 4
print('\n-- Задача 4. Замена всех вложенных списков суммой их элементов --\n')
task4([1, 2, [3, 4], [2, 5, [3, 4, [5]]], [6, 2]])
task4([1, 2, [3, 4], [2, 5, [3, 4, [5]]], [6, 2], [2, 3, [3, [5]]], [9, [0, 8]], 11])
task4([1])
task4([])

# задача 5
print('\n-- Задача 5. Поиск наибольшей возрастающей подпоследовательности в списке --\n')
task5([1, 2, 3, 2, 4, 5, 6, 7])
task5([1, 8, -3, -2, -1, 5, 0, 7])
task5([1, 1, 1])

# задача 6
print('\n-- Задача 6. Текст зАбОрЧиКоМ --\n')
task6('Если я тебе не нравлюсь – застрелись, я не исправлюсь!!!')
task6('аааааааааааааааааааааааааааааааааааааа')
task6('')

# задача 7
print('\n-- Задача 7. Ромб по заданной высоте и ширине --\n')
# было бы гораздо проще и красивее, если бы нужно было вводить только одно значение...................
task7(1, 1)
task7(4, 3)
task7(5, 6)
task7(13, 5)
task7(6, 14)
task7(11, 11)
task7(11, 21)

# задача 8
print('\n-- Задача 8. Таблица Пифагора заданной размерности --\n')
task8(4)
task8(10)
task8(1)
task8(0)

# задача 9
print('\n-- Задача 9. Сумма чисел в строке (через int())  --\n')
task9('10 арбузов и 5 апельсинов')
task9('35 4450арбузов и5 5апельсинов5')
task9('456jjjj345')
task9('fff')
task9('')

# задача 10
print('\n-- Задача 10. Сумма чисел в строке (через map())--\n')
task10('10 арбузов и 5 апельсинов')
task10('35 4450арбузов и5 5апельсинов5')
task10('456jjjj345')
task10('fff')
task10('')
