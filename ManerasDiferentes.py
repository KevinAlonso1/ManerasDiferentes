__author_='Kevin Alonso'

n=15

def factorial(n):
     while n!=1:
       return n * factorial(n-1)

     return 1

print('Diferentes maneras de calcular r: ',n)
print()
print(n,'=',factorial(n))
