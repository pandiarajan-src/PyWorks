# Greatest common divisior

a = int(input("Enter a: "))
b = int(input("Enter b: "))
while b != 0:
    a, b = b, a%b

print(f"GCD is {a}")