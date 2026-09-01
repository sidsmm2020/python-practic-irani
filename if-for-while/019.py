

number = int(input("Enter a number :"))

sum_of_divisors_even = 0

for j in range(2,number + 1,2):
    if number % j == 0:
        sum_of_divisors_even += j

print(f"sum of divsors even = {sum_of_divisors_even}")