from application.salary import calculate_salary
from application.find_date import find_current_date
from application.db.people import get_employees
from application.db.city_data import create_city_data


if __name__ == '__main__':
    print("Start methond main")
    calculate_salary()
    get_employees()
    find_current_date()
    create_city_data()
    print("Finish methond main")
