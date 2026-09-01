

number = int(input("Enter a number :"))

count_of_divisors_even = 0

for j in range(2,number + 1,2):
    if number % j == 0:
        count_of_divisors_even += 1

print(f"count of divsors even = {count_of_divisors_even}")