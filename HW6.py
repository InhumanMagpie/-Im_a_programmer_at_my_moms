import json
import csv
import xlsxwriter


def json_csv_excel_txt_creator():
    """Create json csv excel txt files with age and name"""
    data = input("Введите имя и возраст: ")

    with open('name_age.json', 'w') as file:
        name_age = json.dumps(data)
        file.write(name_age)

    with open('name_age.csv', "w") as file:
        writer = csv.writer(file)
        writer.writerow([data])

    with xlsxwriter.Workbook("name_age.xlsx") as workbook:
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', data)

    with open("name_age.txt", "w") as my_file:
        my_file.write(data)

    with open("name_age.txt", "r") as my_file:
        x = my_file.read()
        print(x)


json_csv_excel_txt_creator()


def codecs_changer(file_name: str, codec_now: str, codec_after: str) -> None:
    with open(file_name, "r", encoding=codec_now) as read_stream:
        text = read_stream.read()
        print(text)
    with open(file_name, "w", encoding=codec_after) as write_stream:
        write_stream.write(text)


codecs_changer("name_age.txt", "utf-8", "ASCII")

