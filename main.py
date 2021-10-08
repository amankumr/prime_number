num = int(input('Enter any Number: '))
for i in range(2,num):
    if num % i == 0:
        print(f'{num} Not Prime Because it is Divisible by {i} at {num//i}.')
        break
else:
    print(f'{num} is a Prime Number.')
    
