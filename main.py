years = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык",
         "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца"]

while True:
    year = int(input('Введите год: '))
    print(years[year % 12])
