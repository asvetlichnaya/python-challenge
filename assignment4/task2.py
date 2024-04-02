from statistics import mean

name_to_salary_dictionary = {
    'Adam': 10000,
    'Beata': 12000,
    'Jarek': 7000,
    'Agnieszka': 8500,
    'Marek': 11200,
    'Ania': 9300,
    'Piotr': 15100,
    'Mateusz': 18000,
    'Agata': 16400,
    'Marian': 11000
}

mean_salary = mean(name_to_salary_dictionary.values())
print('Salaries greater than mean salary: ', mean_salary)

for i in name_to_salary_dictionary:
    if name_to_salary_dictionary[i] > mean_salary:
        print(i, ' ', name_to_salary_dictionary[i])