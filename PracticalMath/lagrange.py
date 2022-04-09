# Lagrange interpolation method
"""
From the given table determine/estimate the value of y, 
when x=2.3 using Lagrange interpolation method
x= 1.1, 1.7, 3.0
f(x)=y=10.6, 15.2, 20.3
"""
n=int(input("Enter how many data points?: "))
x=[]
y=[]
for i in range(n):# range function starts from 0 to n-1
    p=float(input(f"Enter x[{i}]: "))
   
    q=float(input(f"Enter y[{i}]: "))
    x.append(p)# method to add values to list
    y.append(q)
xp=float(input("Enter the value of independent variable: "))
               
yp=0.0 #initialize yp to 0.0
for i in range(n):
    p=1
    for j in range(n):
        if(i!=j):
            p*=(xp-x[j])/(x[i]-x[j])
    yp+=p*y[i]
print(f"\nThe interpolated point corresponding to {xp:.2f} is {yp:.9f}")