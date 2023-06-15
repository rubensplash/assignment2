numbers = input("Enter a list of numbers (separated by spaces): ").split()
numbers = [int(num) for num in numbers]

sum_positive = 0

for num in numbers:
    if num < 0:
        continue
    sum_positive += num

print("Sum of positive numbers:", sum_positive)

