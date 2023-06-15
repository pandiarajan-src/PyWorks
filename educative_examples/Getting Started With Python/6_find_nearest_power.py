
# def nearest_power(n):
#     if n <= 0:
#         return -1 # indicates invalid
#     mindifference = float('inf')
#     nearestpower = 1
#     powervalue = 2
#     while power <= n:
#         diff = abs(power -n)
#         if diff < mindifference:
#             mindifference = diff
#             nearestpower = power
#         power *= 2
#     return nearestpower

def nearest_power(n):
    if n <= 0:
        return -1
    power = 1
    powervalue = 2
    prevpowervalue = 2
    while powervalue <= n:
        prevpowervalue = powervalue
        powervalue *= 2
        power += 1
    return prevpowervalue if (n-prevpowervalue) <= (powervalue -n) else powervalue


number = int(input("Enter the number to find nearest power of 2: "))
print(f"{number} nearest power of 2 is : {nearest_power(number)}")
