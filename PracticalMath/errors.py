
# Program to find the absolute error and relative error
def errors(x, xa):
    abse=abs(x-xa)
    rele=abse/abs(x)
    print("\nFinding absolute and relative errors")
    print("-"*40)
    print()
    print(f"Absolute Error= {abse:.9f}")
    print(f"Relative Error= {rele:.9f}")
    
ev=float(input("Enter exact value: "))
av=float(input("Enter approximate value: "))
errors(ev,av)