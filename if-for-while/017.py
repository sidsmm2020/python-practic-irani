

number = int(input("Enter a number :"))

sum_divisors_odd = 0

for i in range(1,number+1,2):
    if number % i == 0:
        sum_divisors_odd+=i

print(f"sum_divisors_odd = {sum_divisors_odd}")