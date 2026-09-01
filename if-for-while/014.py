

number = int(input("Enter a number : "))

for j in range(2,number+1,2):
    if number%j==0:
        print(j)