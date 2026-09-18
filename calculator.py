def add (P, Q):
    return P + Q

def subtract (P , Q):
    return P-Q

def multiply (P,Q):
    return P * Q

def divide (P,Q):
    return P/Q


print ("please select ur operation...")
print("A. Add")
print("B. Subtract")
print("C. Multiply")
print("D. Divide")


choice=(input("please select your choice A/ B/ C/ D:  "))
num1=input("please enter first number: ")
num2=input("please enter second number: ")

if choice == 'A':
    print(num1, "+" ,num2, "+", add(num1,num2))

elif choice == 'B':
    print(num1, "-" ,num2,"+", subtract(num1,num2))

elif choice == 'C':
    print(num1, "*" ,num2, "=" ,multiply(num1,num2))

elif choice =='D':
    print(num1, "/" ,num2, "=", divide(num1,num2))

else:
    print("this is invalid")
    

