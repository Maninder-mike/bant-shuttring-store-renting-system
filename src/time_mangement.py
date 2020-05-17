from datetime import datetime
import calendar

def calculateAge(birthDate):
    today = datetime.date.today()
    age = today.year - birthDate.year-((today.month, today.day) < (birthDate.month, birthDate.day))
    return age


def birthCalendar(year):
    return calendar.calendar(year)

def today():
    return datetime.now().strftime('%d-%m-%Y')


# print(calculateAge(date(1992, 7, 13)), 'Years')
# print(birthCalendar(1992))
print(today())