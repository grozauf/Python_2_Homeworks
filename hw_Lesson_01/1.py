str_1 = "разработка"
str_2 = "сокет"
str_3 = "декоратор"

print(str_1, type(str_1))
print(str_2, type(str_2))
print(str_3, type(str_3))

bstr_1 = b'\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'  # получено в branah.com, в поле utf-16
print(bstr_1.decode("utf-16"), type(bstr_1)) # почему-то выводит кривые символы
bstr_2 = b'\u0441\u043e\u043a\u0435\u0442'
print(bstr_2.decode("utf-16"), type(bstr_2))
bstr_3 = b'\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
print(bstr_3.decode("utf-16"), type(bstr_3))
