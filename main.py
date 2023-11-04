from datetime import date, datetime, timedelta

def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання
    # Дізнаємося поточну дату
    now = date.today()
    #Створюємо словник з днями тижня
    WEEKDAYS = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
#Створюємо словник, де ключі - це дні тижня, а значення - це порожні списки.
    coworkers_birthdays = {day:[] for day in WEEKDAYS.values()}

#Перебираємо список користувачів.
    for user in users:
        name = user["name"]
        birthday = user["birthday"]
    
# Замінює рік дня народження користувача на поточний рік
        new_birthday = birthday.replace(year=now.year)
    
# Дізнаємось чи було вже день народження в цьому році
        if new_birthday < now:
            new_birthday = new_birthday.replace(year=now.year + 1)
   
# Перевіряємо, чи дата народження потрапляє в наступний тиждень       
        if now <= new_birthday <= now + timedelta(days=7):
            day_of_week = new_birthday.weekday()
            day_name = WEEKDAYS[day_of_week]

# Перевірка, чи день народження падає на вихідний, якщо так то переносимо на понеділок
            if day_name in ["Saturday", "Sunday"]:
                day_name = "Monday"
# Додаємо день народження до відповідного списку
            coworkers_birthdays[day_name].append(name)
# Видаляємо дні, коли немає днів народження
    coworkers_birthdays = {day: names for day, names in coworkers_birthdays.items() if names}
    return coworkers_birthdays



if __name__ == "__main__":
        users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Guido van Rossum", "birthday": datetime(1956, 1, 31).date()},
        {"name": "Bill Gates", "birthday": datetime(1955, 10, 28).date()},
        {"name": "Steve Jobs", "birthday": datetime(1955, 2, 25).date()}
        ]

        result = get_birthdays_per_week(users)
        print(result)
        # Виводимо результат
        for day_name, names in result.items():
            print(f"{day_name}: {', '.join(names)}")
