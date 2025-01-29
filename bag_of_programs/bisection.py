# Bisection Method Analysis Numeric 
# Sesi 14 - Scientific Computing 
# Ludy Hasby Aulia - 2702409305

import math

def function_x(x):
    return x**3 - x -2

def bisection(x1, x2, error_tolerance=0.0001):
    f1 = function_x(x1)
    f2 = function_x(x2)
    if(f1==0):
        return x1
    elif(f2==0):
        return x2
    elif(f1 * f2 > 0):
        print("Interval Has No Root !")
        return
    
    n = int(math.ceil(math.log(abs(x2-x1)/error_tolerance)/math.log(2)))
    
    for i in range(n):
        print(f"\nInteration {i+1}/{n} : ......................")
        x_temp = (x1+x2)/2
        f_temp = function_x(x_temp)

        if(f_temp == 0):
            return x_temp
        if(f2*f_temp <0):
            x1 = x_temp
            f1 = f_temp
        else:
            x2 = x_temp
            f2 = f_temp
        print(f"x1: {x1}, x2: {x2}, max_error: {max([f1-0, f2-0])}")
    print(f"Root Solved at {(x1+x2)/2:.4f}")
    return (x1+x2)/2


if __name__ == "__main__":
    a = 1
    b = 2
    x = bisection(a, b)
