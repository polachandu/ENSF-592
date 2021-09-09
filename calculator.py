# calculator.py
# Chandrahas_Reddy_Pola
#
# A terminal-based calculator application for determining the result of a mathematical expression containing three values and two operators.
# Detailed specifications are provided via the Assignment 2 git repository.
#
# This function tells whether the input is integer or not
#it takes input as integer
#it returns boolean values
def check_user_num(i):
    if i.lstrip('-+').isdigit():
        return 0
    else:
        return 1
# This function tells whether the input is operator or not
#it takes input as operatoe
#it returns boolean values
def check_user_operator(i):
    d=["/", "*", "+", "-"]
    exists= i in d
    if exists:
        return 0
    else:
        return 1


# This function tells about the operator preference 
#it takes input as operator
#it returns boolean values
def operator_preference(a,b):
    x=["/", "*", "+", "-"]
    if num1==x[0] or num2==x[1]:
        return 0
    elif num1==x[0] or num2==x[1]:
        return 1
    else:
        return 0

# This function gives the calcualtion according to operator
#it takes input as two number and one operator
#it returns calculated values
def res_compute(num1,num2,op1):
    if op1=="*":
        return num1*num2
    elif op1=="/":
        return num1/num2
    elif op1=="+":
        return num1+num2
    elif op1=="-":
        return num1-num2

# This function tells how the calculation should be done based on arthimatic operator
#it takes input as three digits and two operators and y value as 0 or 1
#it returns sol
def arithmetic_oper(num1,num2,num3,op1,op2,y):
    if y==1:
        sol=res_compute(num2,num3,op2)
        sol=res_compute(num1,sol,op1)
    else:
        sol=res_compute(num1,num2,op1)
        sol=res_compute(sol,num3,op2)
    
    return sol        


# Main function
#If input values doesn't match with parameters it prompts to give the correct input
#It displays the correct calculation
num1 = (input('Enter your 1st number: '))
while check_user_num(num1)>0: 
    num1 = input('Please re-enter a valid 1st number: ')

op1 = input('Enter 1st operator: ')
while check_user_operator(op1)>0:
    op1 = input('Please re-enter a valid 1st operator: ')
    
num2 = input('Enter your 2nd number: ')
while check_user_num(num2)>0:
    num2 = input('Please re-enter a valid 2nd number: ')

op2 = input('Enter 2nd operator: ')
while check_user_operator(op2)>0:
    op2 = input('Please re-enter a valid 2nd operator: ')

num3 = input('Enter your 3rd number: ')
while check_user_num(num3)>0:
    num3 = input('Please re-enter a valid 3rd number: ')

num1=int(num1)
num2=int(num2)
num3=int(num3)
y=operator_preference(op1,op2)
print("The result is " + str(num1) +' '+ op1 +' '+ str(num2) +' '+ op2 +' '+ str(num3) +' '+ '=' + ' '+str(arithmetic_oper(num1,num2,num3,op1,op2,y)))