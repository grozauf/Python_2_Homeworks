import csv
import yaml

items = []


def convert_to_yaml(line):
    item = {
     'id': int(line[0]),
     'title_english': line[1],
     'title_russian': line[2]
    }
    items.append(item)


print("считываем данные из файла 5_in.csv")
with open("5_in.csv", "r") as in_file:
    reader = csv.reader(in_file)
    next(reader) # skip headers
    for line in reader:
        print(line)
        convert_to_yaml(line)

print("записываем данные в файл 5_out.yaml")
with open("5_out.yaml", "w", encoding="utf-8") as out_file:
    out_file.write(yaml.dump(items, default_flow_style=False, allow_unicode=True))

print("проверка записанных данных:")
with open('5_out.yaml', encoding="utf-8") as f_n:
    print(f_n.read())