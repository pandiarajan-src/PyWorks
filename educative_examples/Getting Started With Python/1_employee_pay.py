hours = float(input("Enter the number of hours worked this week: "))
rate = float(input("Enter rate per hour: "))
salary = 0.0

if hours > 40:
    regular_salary = rate * 40
    overtime_salary = rate * 1.5 * (hours - 40)
    print(f"Regular pay: {regular_salary}")
    print(f"Overtime pay: {overtime_salary}")
    print(f"Total pay: {regular_salary + overtime_salary}")
else:
    regular_pay = rate * hours
    print(f"Regular pay: {regular_pay}")


