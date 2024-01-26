import datetime
from datetime import datetime as dtdt


def get_upcoming_birthdays(users):   
    current_day = dtdt.now().date()
    upcoming_birthdays = []

    for user in users:
        birthday_datetime = dtdt.strptime(user['birthday'], "%Y.%m.%d").date()
        birthday_this_year = dtdt(current_day.year, birthday_datetime.month, birthday_datetime.day).date()

        if birthday_this_year < current_day:
            birthday_this_year = dtdt(current_day.year + 1, birthday_datetime.month, birthday_datetime.day).date()
        
        days_till_birthday = (birthday_this_year - current_day).days

        if 0 <= days_till_birthday <=7:
            if birthday_this_year.weekday() == (5 or 6):
                monday_after_birthday = birthday_this_year + datetime.timedelta(days=(7-birthday_this_year.weekday()))
                congratulation_date = monday_after_birthday.strftime("%Y.%m.%d")
            else:
                congratulation_date = birthday_this_year.strftime("%Y.%m.%d")

            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date})
    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.01.30"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
    ]
result = get_upcoming_birthdays(users)
print(result)