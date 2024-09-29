import datetime
from salary import calculate_salary
from people import get_employees

date_time = datetime.datetime.today()

if __name__ == '__main__':
    calculate_salary(1000, 3000)
    get_employees(1)
    print(date_time)
