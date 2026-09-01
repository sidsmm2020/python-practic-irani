

number = int(input("Enter a number :"))
divisors_count = 0
for divisor in range(1,number+1):
    if number%divisor == 0:
        divisors_count += 1

print(f"divisors Count = {divisors_count}")