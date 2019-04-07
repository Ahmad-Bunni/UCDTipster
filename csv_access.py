import csv
from datetime import datetime

class CsvFile(object):
    def __init__(self):
        self.filename = 'results.csv'


    def read(self):
        bets_list = []
        with open(self.filename) as csv_file:
            csv_reader = csv.reader(csv_file, skipinitialspace=True, delimiter=',', quoting=csv.QUOTE_NONE)
            for row in csv_reader:
                bets_list.append(row)

            return bets_list


    def write (self, fields_array):
        with open(self.filename, "a",newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(fields_array)
