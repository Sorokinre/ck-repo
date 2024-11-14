# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, "r") as csv_file, open(OUTPUT_FILENAME, "w") as json_file:
        csv_reader = csv.DictReader(csv_file)
        data_list = []
        for row in csv_reader:
            data_list.append(row)

        # TODO Сериализовать в файл с отступами равными 4
        json.dump(data_list, json_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
