# Задание 1

phrase_1 = input("Введите первую фразу: ")
phrase_2 = input("Введите вторую фразу: ")
if len(phrase_1) > len(phrase_2):
    print("Первая строка длиннее")
elif len(phrase_2) > len(phrase_1):
    print("Вторая строка длиннее")
else:
    print("Строки одинаковой длины")

# Задание 2

import calendar

year = int(input("Введите год: "))
if calendar.isleap(year):
    print(f"{year} - високосный")
else:
    print(f"{year} - не високосный")

# Задание 3

def get_zodiac(month, day):
    if (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Козерог"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Водолей"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Рыбы"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Овен"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Телец"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
        return "Близнецы"
    elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
        return "Рак"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Лев"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Дева"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 23):
        return "Весы"
    elif (month == 10 and day >= 24) or (month == 11 and day <= 22):
        return "Скорпион"
    elif (month == 11 and day >= 23) or (month == 12 and day <= 21):
        return "Стрелец"

# Словарь месяцев 
month_names = {
    'январь': 1, 'февраль': 2, 'март': 3, 'апрель': 4,
    'май': 5, 'июнь': 6, 'июль': 7, 'август': 8,
    'сентябрь': 9, 'октябрь': 10, 'ноябрь': 11, 'декабрь': 12
}

# Ввод месяца
while True:
    month_input = input("Введите месяц рождения. Доступные варианты: январь, февраль, март, апрель, май, июнь, июль, август, сентябрь, октябрь, ноябрь, декабрь").strip().lower()
    
    if month_input in month_names:
        month = month_names[month_input]
        break
    else:
        print("Ошибка! Введите корректное название месяца.")

# Ввод дня
while True:
    try:
        day = int(input(f"Введите день рождения: "))
        
        days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        if 1 <= day <= days_in_month[month - 1]:
            break
        print(f"Ошибка! День должен быть от 1 до {days_in_month[month - 1]}.")
    except ValueError:
        print("Ошибка! Введите целое число.")

zodiac_sign = get_zodiac(month, day)

print(f"\nВаш знак зодиака: {zodiac_sign}")

# Задание 4

def get_package_type(width, length, height):
    
    # если каждое из трех измерений менее или равно 15 сантиметрам
    if width <= 15 and length <= 15 and height <= 15:
        return "Коробка №1"
    
    # если хотя бы одно из измерений больше 2 метров
    if width > 200 or length > 200 or height > 200:
        return "Упаковка для лыж"
    
    # если хотя бы одно из измерений больше 15 сантиметров, но менее 50 сантиметров
    if (15 < width < 50) or (15 < length < 50) or (15 < height < 50):
        return "Коробка №2"
    
    # все остальные случаи
    return "Коробка №3"

width = float(input("\nШирина (см): "))
length = float(input("\nДлина (см): "))
height = float(input("\nВысота (см): "))

print(f"Упаковка: {get_package_type(width, length, height)}")

# Задание 5

def is_lucky_ticket(number):
    num_str = str(number)
    sum_first = sum(int(digit) for digit in num_str[:3])
    sum_second = sum(int(digit) for digit in num_str[3:])
    
    return sum_first == sum_second

number = int(input("\nВведите шестизначный номер билета: "))

if is_lucky_ticket(number):
    print("\nСчастливый билет!")
else:
    print("\nНесчастливый билет")