import yaml

print("чтение данных из yaml")
with open('3_in.yaml') as f_n:
    f_n_content = yaml.load(f_n)
print(f_n_content)

print("записываем данные в файл 3_out.yaml")
action_list = ['msg_1', 'msg_2', 'msg_3']

to_list = ['account_1', 'account_2', 'account_3']

data_to_yaml = {'action' : action_list, 'to' : to_list}

with open('3_out.yaml', 'w') as f_n:
    yaml.dump(data_to_yaml, f_n)

print("проверка записанных данных:")
with open('3_out.yaml') as f_n:
    print(f_n.read())