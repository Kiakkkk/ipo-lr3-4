corr_pass = "qwerty123456"   #изначальный пароль
print("Введите пароль: ")
password = input()
if  corr_pass == password:
    print("Доступ разрешен")
else:
    print("Доступ запрещён")
