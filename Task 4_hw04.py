from datetime import datetime, timedelta




def get_upcoming_birthdays(users: list) -> list:
    upcoming_birthdays = []
    today = datetime.now().date()
    for user in users:
        birthday = (datetime.strptime(user["birthday"], "%Y.%m.%d").date()).replace(year=today.year)

        if birthday < today:
            birthday = birthday.replace(year = today.year + 1)

        if today < birthday <= today + timedelta(days=7):
            # print(birthday.weekday())
            if birthday.weekday() == 5:

                congratulation_date = (birthday + timedelta(days=2)).strftime("%Y.%m.%d")
            elif birthday.weekday() == 6:

                congratulation_date = (birthday + timedelta(days=1)).strftime("%Y.%m.%d")
            else:

                congratulation_date = birthday.strftime("%Y.%m.%d")
            upcoming_birthdays.append({"name": user["name"], 'congratulation_date': congratulation_date})
    return upcoming_birthdays

if __name__ == "__main__":
    users = [
        {"name": "John Smith", "birthday": "1985.01.23"},
        {"name": "Jane Bond", "birthday": "1990.01.27"},
        {"name": "Samanta Johnson", "birthday": "1979.03.15"},
        {"name": "Yuliya Kostenko", "birthday": "1998.03.14"},
        {"name": "Hunny Bunny", "birthday": "1983.03.16"},
        ]
    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming_birthdays)
