from csv import reader
import sys
import time


def scan_file(filename):
    list_of_keywords = ["2000", "2100"]
    with open(filename, 'r') as read_obj:
        csv_reader = reader(read_obj)
        count0 = 0
        count1 = 0
        counter = 0
        for row in csv_reader:
            if row[5] == list_of_keywords[0]:
                count0 += 1
            if row[5] == list_of_keywords[1]:
                count1 += 1
            counter += 1
        print(count0)
        print(count1)
        print(counter)


filename = sys.argv[1]
time1 = time.time_ns()
scan_file(filename)
time2 = time.time_ns()
