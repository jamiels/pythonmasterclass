def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)


factorial_of_five = factorial(5)
print('The factorial of five is',factorial_of_five)

factorial_of_ten = factorial(10)
print('The factorial of ten is',factorial_of_ten)

print('The factorial of six is',factorial(6))

f = factorial(7)
print('The factorial of seven is',f)

f = factorial(9)
print('9! is ',f)
