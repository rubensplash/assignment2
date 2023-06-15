sum = 0

while True:
    num = int(input("Enter a number (enter a negative number to stop): "))
    if num < 0:
        break
    if num > 0:
        sum += num

print("Sum of positive numbers:", sum)
