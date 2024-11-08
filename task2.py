# TODO Напишите функцию find_common_participants
def common_elements(a, b, с=","):
    result = []
    a = a.split(с)
    b = b.split(с)

    for item1 in a:
        for item2 in b:
            if item1 == item2:
                result.append(item1)

    result = sorted(set(result))  # Удаляем дубликаты и сортируем
    return result


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Проверьте работу функции с разделителем отличным от запятой
print(common_elements(participants_first_group, participants_second_group, "|"))
