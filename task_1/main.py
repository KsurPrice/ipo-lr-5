glassn = "аеёиоуыэюяАЕЁИОУЫЭЮЯ" # Список русских гласных
sogl = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"# Список русских согласных
text = input("Введите строку на русском: ")# Ввод строки от пользователя
length = len(text)# Подсчёт длины
glassn_count = sum(1 for char in text if char in glassn)# Подсчёт гласных
sogl_count = sum(1 for char in text if char in sogl)# Подсчёт согласных
# Вывод результатов
print("Длина строки:", length)
print("Гласных букв:", glassn_count)
print("Согласных букв:", sogl_count)