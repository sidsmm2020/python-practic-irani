


number = int(input("Enter a number : "))

divisor_counter = 0
sum_divisor = 0

for i in range(1,number+1):
    if number % i == 0:
        divisor_counter += 1
        sum_divisor += i
# division by zero sometime happen
avg = sum_divisor/divisor_counter

print(f"avg_of_divisors = {avg}")