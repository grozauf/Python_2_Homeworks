import csv
import json

template = '{{"ФИО": "{}", "e-mail": "{}", "ЕГЭ": {{"ИКТ": {}, "общий": {}}}}}'
result = []
print("считывание данных из 4_in.csv:")
with open('4_in.csv') as fin:
    reader = csv.reader(fin)
    for line in reader:
        print(line)
        line = [x if x != '-' else 'null' for x in line]
        result.append(json.loads(template.format(*(' '.join(line[0:3]), *line[3:]))))

print("запись данных в файл 4_out.json")
with open('4_out.json', 'w') as fh:
    fh.write(json.dumps(result, sort_keys=True, ensure_ascii=False, indent=4))

print("проверка записанных данных:")
with open('4_out.json') as f_n:
    print(f_n.read())