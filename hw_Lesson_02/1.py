import csv

print("Чтение данных из csv:")
with open('1_in.csv') as f_n:
    f_n_reader = csv.reader(f_n)
    for row in f_n_reader:
        print(row)

print("Запись данных в файл 1_out.csv")

data = [['hostname', 'vendor', 'model', 'location'],
        ['kp1', 'Cisco', '2960', 'Moscow, str'],
        ['kp2', 'Cisco', '2960', 'Novosibirsk, str'],
        ['kp3', 'Cisco', '2960', 'Kazan, str'],
        ['kp4', 'Cisco', '2960', 'Tomsk, str']]

with open('1_out.csv', 'w', newline='') as f_n:
    f_n_writer = csv.writer(f_n)
    for row in data:
        f_n_writer.writerow(row)

print("Проверка записанных данных:")
with open('1_out.csv') as f_n:
    print(f_n.read())

