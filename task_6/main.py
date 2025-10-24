with open("text.txt", "r", encoding="utf-8") as infile:# Открываем исходный файл для чтения
    lines = infile.readlines()

with open("output.txt", "w", encoding="utf-8") as outfile: # Открываем новый файл для записи
    for i, line in enumerate(lines, start=1):
        # Записываем номер строки и саму строку
        outfile.write(f"{i}: {line}")
