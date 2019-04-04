import json

print("чтение данных из json")
with open('2_in.json') as f_n:
    objs = json.load(f_n)

for section, commands in objs.items():
    print(section, ":", commands)

print("запись данных в файл 2_out.json")

dict_to_json = {
    "action": "msg",
    "to": "account_name",
    "from": "account_name",
    "encoding": "ascii",
    "message": "message"
    }

with open('2_out.json', 'w') as f_n:
    f_n.write(json.dumps(dict_to_json))

print("проверка записанных данных:")
with open('2_out.json') as f_n:
    print(f_n.read())
