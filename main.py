n = int(input('Enter any Number: '))
for i in range(2,n):
    if n % i == 0:
        print(f'{n} Not Prime Because it is Divisible by {i} at {n//i}.')
        break
else:
    print(f'{n} is a Prime Number.')
    
