




number = int(input("Enter a number : "))

divisor_counter_even = 0
sum_divisor_even = 0

for i in range(2,number+1,2):
    if number % i == 0:
        divisor_counter_even += 1
        sum_divisor_even += i
# division by zero sometime happen
avg_even = sum_divisor_even/divisor_counter_even

print(f"avg_of_divisors_even = {avg_even}")