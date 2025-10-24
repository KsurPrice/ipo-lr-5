#Карась Илья
text = input("Введите строку: ")# Ввод строки от пользователя

found = False# Проверка и вывод индексов
for i in range(len(text)):
    if text[i] == 'e':
        print("Индекс буквы 'e':", i)
        found = True

if not found:
    print("Буква 'e' не найдена в строке.")