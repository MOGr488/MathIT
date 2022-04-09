"""
Math for I.T Assignment: 
Question: Write a Python program for finding the solution of a given function ...  with   using Newton Raphson's Method.  

1) find out 3 approximations and print them as a table.

2) Print the last approximate solution. (use 4 digit rounding)

Student Name : --
Studnet ID : -
With The study with student: -

Referance: https://www.codesansar.com/numerical-methods/newton-raphson-method-python-program.htm

"""
#First Importing Math library
import math

# Defining Function
def f(x):
    return (3*math.cos(x)) - math.exp(x)

# Defining derivative of function
def g(x):
    return (-3*math.sin(x)) - math.exp(x)

# Newton Raphson Method
def NewtonRaphson (Xi,N):
    print ("Newton Raphson Method")
    step = 1 
    conditon = True
    while conditon:

        if g(Xi) == 0.0:
            print ("Error: Derivative of f(x) is Zero")
            break
        
        H = f(Xi)/g(Xi)
        Xn = Xi - H

        print('Iteration-%d, X = %0.6f and f(X) = %0.6f' % (step, Xn, f(Xi)))
        Xi = Xn
        step = step + 1

        if step > N:           
            break

        conditon = abs(f(Xn)) > 0.000001

    print ("\nThe Approximated Root is: %0.8f" % Xi)
    


Xi = float (input("Enter inital approximation (P0): "))
N = float (input("Enter The number of iterations (Steps): "))
print ("===="*7)
NewtonRaphson (Xi, N)
