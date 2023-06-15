# Write your code here
print("Enter the number to find an average, enter 0 to stop.")
number = int(input())
sum_value = 0
count = 0
while number != 0:    
    sum_value += number
    number = int(input())
    count += 1

print(f"Average of inputs are: {sum_value/count}")
