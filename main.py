import csv

filename = 'dataset.csv'

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        row_count = len(row)

for column in range(0,row_count):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            # note: a file name cannot contain "/"
            if line_count == 0: f_csv = open(f'{1+column}_{row[column].replace("/", "&")}.csv', 'w')

            if line_count == 1: f_csv.write(f'{row[column]}')

            if line_count > 1: f_csv.write(f',{row[column]}')
            
            line_count += 1

        print(f'Processed file number {1+column} named {f_csv.name} with {line_count} lines.')