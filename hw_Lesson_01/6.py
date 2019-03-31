import locale

test_file = open("test_file.txt", "w")

test_file.write("сетевое программирование\n")
test_file.write("сокет\n")
test_file.write("декоратор\n")
print(test_file)
test_file.close()

def_coding = locale.getpreferredencoding()
print("кодировка файлов по умолчанию =", def_coding)

print("Содержимое файла в Unicode:")
with open("test_file.txt", encoding="utf-16le") as f_n:
    for el_str in f_n:
        print(el_str, end='')
