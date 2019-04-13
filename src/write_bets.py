from src import csv_access
from calendar import monthrange
from datetime import datetime


def get_race_course():
    race_course = input('Enter race course: ')
    while race_course.strip() == '':
        race_course = input('Please enter a valid race course: ')
    return race_course

def get_horse_name():
    horse_name = input('Enter horse name: ')
    while horse_name.strip() == '':
        horse_name = input('Please enter a valid horse name: ')
    return horse_name

def get_race_year():
    year = 0
    currentYear = datetime.now().year
    while not 1900 <= year <= currentYear:
        try:
            year = int(input("{}{}{}".format('Please enter the race year between 1900 and ', currentYear, ': ')))
        except:
            year = 0
    return year;

def get_race_month():
    month = 0
    while not 0 < month <= 12:
        try:
            month = int(input('Please enter the race month between 1 and 12: '))
        except:
            month = 0

    return month;

def get_race_day(year, month):
    day = 0
    range = monthrange(year, month)

    while not 0 < day <= range[1]:
        try:
            day = int(input("{}{}{}".format('Please enter the race day between 1 and ', range[1], ': ')))
        except:
            day = 0

    return day;

def get_bet_amount():
    bet_amount = 0.0
    try:
        bet_amount = float(input('Please enter the bet amount: '))
    except:
        bet_amount = 0.0

    while bet_amount <= 0:
        try:
            bet_amount = float(input('Please enter a valid bet amount: '))
        except:
            bet_amount = 0.0
    return bet_amount

def get_bet_result():
    is_won = 0
    while not 0 < is_won <= 2:
        try:
            is_won = int(input("Please enter '1' if the bet was won and '2' if the bet was lost: "))
        except:
            is_won = 0

    if is_won == 1:
        result = "won"
    else:
        result = "loss"

    return result

def record_new_bet():

    race_course = get_race_course()

    horse_name = get_horse_name()

    year = get_race_year()

    month = get_race_month()

    day = get_race_day(year,month)

    bet_amount = get_bet_amount()

    bet_result = get_bet_result()

    csv_access.CsvFile().write([race_course.strip(), horse_name.strip(), year,
                                "{:02d}".format(month),
                                "{:02d}".format(day),
                                bet_amount, bet_result])

    print('-- A new bet has been recorded --')


