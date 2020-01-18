from datetime import datetime, timedelta

print(f"Today's date is {str(datetime.now())}")
print(f"Yesterday's date is {str(datetime.now() - timedelta(days=1))}")
print(f"Last week's this day is {str(datetime.now() - timedelta(weeks=1))}")

birth_date_as_string = input("Enter  your Birthday in the following format dd/mm/yyyy : ")
birth_date = datetime.strptime(birth_date_as_string, '%d/%m/%Y')
print(f"your birthday is {str(birth_date)}")
bday_string = "your birthday short is {0:%d}-{0:%B}-{0:%Y}".format(birth_date)
print(bday_string)
