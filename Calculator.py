def multiply(P,Q):
    return P*Q
def addition(P,Q):
    return P+Q
def subtraction(P,Q):
    return P-Q
def divide(P,Q):
    return P/Q
def square(P,Q):
    return P**Q

print('PLease select the operation')
print('\na. Addition')
print('b. Subtraction')
print('c. Multiplication')
print('d. Division')
print('e. Square')

choice=input('\nPlease enter the choice a/b/c/d/e: ')

num1=int(input('Enter the first number: '))
num2=int(input('Enter the second number: '))

if choice=='a':
    print(num1,'+',num2,'=',addition(num1,num2))
elif choice=='b':
    print(num1,'-',num2,'=',subtraction(num1,num2))
elif choice=='c':
    print(num1,'*',num2,'=',multiply(num1,num2))
elif choice=='d':
    print(num1,'/',num2,'=',divide(num1,num2))
elif choice=='e':
    print(num1,'^',num2,'=',square(num1,num2))
else:
    print('Invalid Choice')