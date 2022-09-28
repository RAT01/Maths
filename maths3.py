import cmath

a = complex(input("Enter your First Number"))
b = complex(input("Enter your Second Number"))
print(a.real)
print(a.imag)
c=a.conjugate()
print('Conjugate of a is :-',c)
d=complex(a+b)
e=complex(a-b)
print("Sum of complex are: ", d)
print("different of complex number:-",e)
