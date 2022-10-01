def sort_array(source_array):  # на вход всегда поступает лист из int значений

    # Создадим списки, в которые будут поступать отсортированные по четности значения и их индексы
    i_list_odd = []  # нечетные индексы
    i_list_even = []  # четные индексы
    i_count_odd = 0
    i_count_even = 0

    j_list_odd = []  # нечетные значения
    j_list_even = []  # четные значения

    result_list = []  # сюда собирается результат

    for i, j in enumerate(source_array):
        if j % 2 == 0:
            i_list_even.append(i)
            j_list_even.append(j)
        else:
            i_list_odd.append(i)
            j_list_odd.append(j)
    j_list_odd.sort()


    for i in j_list_odd:
        result_list.insert(i_list_odd[i_count_odd], i)
        i_count_odd += 1

    for i in j_list_even:
        result_list.insert(i_list_even[i_count_even], i)
        i_count_even += 1
    print(result_list)
    return result_list


list_1 = [11, 2, 7, 4, 9, 6, 3, 8, 5, 10]
sort_array(list_1)


# Решение было куда проще

def sort_array_2(source_array_2):
    # Задается переменная результата в которую будут заливаться все значения из source_array по порядку.
    # При этом сразу происходит сортировка всех l элементов из source_array, если этот элемент odd.
    result = sorted([l for l in source_array_2 if l % 2 == 1])

    # enumerate выдает значения enumerate(индекс, значение)
    for index, item in enumerate(source_array_2):
        if item % 2 == 0:
            result.insert(index, item)
    print(result)
    return result


list_2 = [111, 2, 7, 4, 69, 6, 3, 8, 5, 10]
sort_array_2(list_2)
