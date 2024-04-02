import csv


with open('input_files/5_input.csv') as file:
    content = csv.DictReader(file)
    for row in content:
        if int(row['Duration of employment in years']) >= 5:
            print('Name: ', row['Name'], ' - compensation: ', int(row['Duration of employment in years'])*1000)
