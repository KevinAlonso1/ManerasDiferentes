__author_='Kevin Alonso'
r=6
n=7
c=0
def factorial(n):
     while n!=1:
        return n * factorial(n-1)

     return 1
def factorial(r):
    while r!=1:
        return r*factorial(r-1)

    return 1
c=   (int) (factorial(n)*factorial(r)*factorial(n - r))

print('Diferentes maneras de calcular ')
print('Numero r','=',r)
print('Numero n','=',n)
print()
print(n,'=',factorial(n))
print(r,'=',factorial(r))
print(c)