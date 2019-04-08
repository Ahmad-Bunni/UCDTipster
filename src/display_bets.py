from src import csv_access, write_bets
from collections import defaultdict
from datetime import datetime
from datetime import timedelta

def all():
     bets_list = csv_access.CsvFile().read()
     for row in bets_list:
         print(row)

def yearly_report():

    bets_list = csv_access.CsvFile().read()

    d = defaultdict(lambda: [0, 0])
    for row in  sorted(bets_list, key=lambda x:x[2]):

        if row[6] == 'won': d[row[2]][0] += float(row[5])
        if row [6] == 'lost': d[row[2]][1] +=  float(row[5])

    print('-- Yearly Report -- ')
    print('Year', ' | Total Won | ', "Total Lost")
    for key,value in d.items():
        print(key,
              " " *(7-len(key)),
              '{}{}'.format('€', value[0]),
              " "*(10-len(str(value[0]))),
              '{}{}'.format('€', value[1]))

def most_popular_course():
    bets_list = csv_access.CsvFile().read()

    d = defaultdict(lambda: [0])
    for row in sorted(bets_list, key=lambda x: x[0]):
        d[row[0]][0] += 1

    popular_course  = max(d.items(),key=lambda item:item[1])
    print('{}{}{}{}{}'.format('The most popular race course is ', popular_course[0], ' with a total of ', popular_course[1][0], ' placed bets'))

def bets_by_date():
    bets_list = csv_access.CsvFile().read()
    bets_list =  sorted(bets_list, key = lambda x: (x[2], x[3], x[4]))

    for bet in bets_list:
        print(bet)

def highest_bets():

    bets_list = csv_access.CsvFile().read()

    won_bets = [bet for bet in bets_list if bet[6] == 'won']
    lost_bets  = [bet for bet in bets_list if bet[6] == 'lost']

    max_won  = max(won_bets, key=lambda item: float(item[5]))
    max_lost  = max(lost_bets, key=lambda item: float(item[5]))

    print('{}{}'.format('Highest amount won for a bet is: ', max_won[5]))
    print('{}{}'.format('Highest amount lost for a bet is: ', max_lost[5]))

def success_rate():
    bets_list = csv_access.CsvFile().read()

    won_bets = [bet for bet in bets_list if bet[6] == 'won']

    print('{}{}{}{}'.format('UCD Tipster has won ' ,len(won_bets), ' bets out of ', len(bets_list)))
    print('{}{}{}'.format('UCD Tipster has a success rate of ',  len(won_bets)/len(bets_list) * 100,'%'))

def average_spent():

    bets_list = csv_access.CsvFile().read()

    year = write_bets.get_race_year()
    month = write_bets.get_race_month()

    filter_bets = [bet for bet in bets_list if int(bet[2]) == year and int(bet[3]) == month]

    if(len(filter_bets) > 0):
        print('{}{}'.format('The average spent for the given period is: €', sum(float(amount[5]) for amount in filter_bets)/float(len(filter_bets))))

    else:
        print('No records found in the given period')

def average_time():

    bets_list = csv_access.CsvFile().read()

    bets_list = sorted(bets_list, key=lambda x: (x[2], x[3], x[4]),reverse=True)

    dates_list= []

    for bet in bets_list:

        date = datetime.strptime('{}-{}-{}'.format(bet[2],bet[3],bet[4]), '%Y-%m-%d')

        dates_list.append(date)

    sumdeltas = timedelta(seconds=0)
    i = 1
    while i < len(dates_list):
        sumdeltas += dates_list[i - 1] - dates_list[i]
        i = i + 1

    avg_delta = sumdeltas / (len(dates_list) - 1)
    print('{}{}{}'.format('The average time between bets is: ',avg_delta.days, ' day(s)'))