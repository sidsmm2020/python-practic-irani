

number = int(input("Enter a number :"))

divisor_count_odd = 0

for i in range(1,number+1,2):
    if number % i == 0:
        divisor_count_odd+=1

print(f"divisors_count_odd = {divisor_count_odd}")