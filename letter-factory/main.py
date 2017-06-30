import os
import csv

# csv should be located in the same directory
example_file = open('scrap.csv')

reader = csv.reader(example_file)



for row in reader:
    for field in row:
        print(field)
    print('__________________________\n')
