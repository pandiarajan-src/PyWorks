# Write you code below
def isPrime(n):
    prime = True
    if n > 0:
        if n not in [1, 2, 3, 5, 7]:
            if (n%2 == 0) or (n%3 == 0) or (n%5 == 0):
                prime = False
            else:
                for i in range((n ** 0.5)+1):
                    if n % i == 0:
                        prime = False
                        break
    return prime



number = int(input("Enter a number: "))
if isPrime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")