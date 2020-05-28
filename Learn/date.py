'''Experiment on date, time and year fields'''
from datetime import datetime, timedelta #, date

def print_today_yesterday_lw_date():
    """Print today's date, yesterday;s date and last week this day"""
    print(f"Today's date is {str(datetime.now())}")
    print(f"Yesterday's date is {str(datetime.now() - timedelta(days=1))}")
    print(f"Last week's this day is {str(datetime.now() - timedelta(weeks=1))}")

def birthday_prints():
    """print your birthday in different ways"""
    birth_date_as_string = input("Enter  your Birthday in the following format dd/mm/yyyy : ")
    birth_date = datetime.strptime(birth_date_as_string, '%d/%m/%Y')
    print(f"your birthday is {str(birth_date)}")
    bday_string = "your birthday short is {0:%d}-{0:%B}-{0:%Y}".format(birth_date)
    print(bday_string)
    return bday_string, birth_date, birth_date_as_string

def is_leap_year(year_input):
    """Find whether the given year is leap or not"""
    is_leap = False
    try:
        if year_input%400 == 0:
            is_leap = True
        elif (year_input%100 != 0) & (year_input%4 == 0):
            is_leap = True
        else:
            is_leap = False
    except ArithmeticError:
        print("Arithmetic error occured")
    except: # pylint: disable=bare-except
        print("exception occured")
    return is_leap

if __name__ == "__main__":
    #INPUT_YEAR = int(input("Enter year (non -ve & non-zero & non-decimal: "))
    for INPUT_YEAR in [2000, 1959, 2019, 2020, 2008, 2009]:
        print("Year {0} - Is it leap year? {1}".format(INPUT_YEAR, is_leap_year(INPUT_YEAR)))
    birthday_prints()
    print_today_yesterday_lw_date()
