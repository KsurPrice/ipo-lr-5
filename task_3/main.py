#Карась Илья
with open("text.txt", "r", encoding="utf-8") as file:# Открываем файл
    text = file.read()  #считываем содержимое

words = text.split() # Разбиваем текст на слова

print("Количество слов в файле:", len(words))# Выводим количество слов
