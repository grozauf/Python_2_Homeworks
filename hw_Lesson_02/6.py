import json
import yaml

print("чтение данных из json:")
with open('6_in.json') as f_n:
    objs = json.load(f_n)

print(objs)

print("записываем данные в файл 6_out.yaml")
with open("6_out.yaml", "w", encoding="utf-8") as out_file:
    out_file.write(yaml.dump(objs, default_flow_style=False, allow_unicode=True))

print("проверка записанных данных:")
with open('6_out.yaml', encoding="utf-8") as f_n:
    print(f_n.read())