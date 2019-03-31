str_1 = "разработка"
str_2 = "администрирование"
str_3 = "protocol"
str_4 = "standard"

bstr_1 = str_1.encode()
bstr_2 = str_2.encode()
bstr_3 = str_3.encode()
bstr_4 = str_4.encode()

print("encode =", bstr_1, "decode =", bstr_1.decode())
print("encode =", bstr_2, "decode =", bstr_2.decode())
print("encode =", bstr_3, "decode =", bstr_3.decode())
print("encode =", bstr_4, "decode =", bstr_4.decode())