# 1. LEVEL_1_basic Write program that finds max 3 salaries from the list.
# Example:
# input:
# salaries = [10000, 12000, 7000, 8500, 11200, 9300, 15100, 18000, 16400, 11000]
# output: [18000, 16400, 15100]

def get_n_max_salaries(salary, n_max_salaries):
    salary.sort(reverse=True)
    return salary[0:n_max_salaries:1]


salaries = [10000, 12000, 7000, 8500, 11200, 9300, 15100, 18000, 16400, 11000]
output = get_n_max_salaries(salaries, 3)
print(output)
