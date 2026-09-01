

number = int(input("Enter a number :"))

sum_of_divisors = 0

for divisors in range(1,number+1):
    if number%divisors==0:
        sum_of_divisors+=divisors


print(f"sum of divisors = {sum_of_divisors}")