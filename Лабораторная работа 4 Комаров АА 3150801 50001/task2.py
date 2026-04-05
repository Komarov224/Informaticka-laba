# TODO импортировать необходимые молули
import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # TODO считать содержимое csv файла
    data = []
    with open(INPUT_FILENAME, mode="r") as f: #открываем csv файл
        reader = csv.DictReader(f) #читаем как из подсказки с методов Dict
        for row in reader: # по строчк
            data.append(row) #почему то дали пустой csv файл


    with open(OUTPUT_FILENAME, mode="w", encoding='utf-8') as f:
        json.dump(data, f, indent=4) #записываем в файл с 4 отстуопм
    # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
