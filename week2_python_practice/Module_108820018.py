import math

def table9x9():
    for r in range(1, 10):
        for c in range(1, 10):
            print(f"{r}x{c}={r*c:2} ", end="")        
        print()

def fac_table(n):
    fac_tb = ""
    for i in range(n+1):
        fac_tb += f"{i}! = {math.factorial(i)}\n"
    print(fac_tb)

fac_table(23)
table9x9()