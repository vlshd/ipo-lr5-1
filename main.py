def a(s):
    b = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    c = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
    
    num_b = sum(1 for char in s if char in b)
    num_c = sum(1 for char in s if char in c)
    
    return num_b, num_c
user_input = input("Введите строку: ") # запрашиваем строку
dlina = len(user_input) # вычисляем длину
glasnie, soglasnie = a(user_input) # вычисляем количество гласных и согласных

# Выводим результаты
print(f"Длина строки: {dlina}")
print(f"Количество гласных: {glasnie}")
print(f"Количество согласных: {soglasnie}")
