#Bisection method - An iterative method to find a root of a given equation. 

import math
def f(x):
    return math.cos(x)-x*math.e**x
#accept search interval end points in a and b
a=float(input("Enter search interval\'s left end point: "))
b=float(input("Enter search interval\'s right end point: "))
err=0.001
if(f(a)*f(b)>0):
    print("Sorry. The search interval is not correct \nTry with different initial values")
else:
    i=1
    print("\n\nFinding the root of cosx-xe^x using Bisection Method with endpoints 0.0 and 1.0")
    print("-"*53+"\n")
    print("Iterations\t  a\t\t b\t\t m\t   f(a)*f(m)\n")
    print("-"*53+"\n")     
    while(abs(a-b)>err):
        m=(a+b)/2 #find the mid point
        ym=f(m)
        ya=f(a)
        if(ym*ya<0): #if f(m) and f(a) are of different signs then move b 
            print(f"{i:6d}\t\t{a:4.3f}\t{b:.3f}\t{m:.3f}\t{ya*ym:.5f}")
            b=m
        else: #otherwise move a
            print(f"{i:6d}\t\t{a:4.3f}\t{b:.3f}\t{m:.3f}\t{ya*ym:.5f}")
            a=m 
        i+=1
    print("-"*53+"\n")
    x0=(a+b)/2
    print(f"Approximate solution = {x0}")

        
    

