def factorial_iterative(n):
    """
    parameter : n
    return : n * n-1 * n-2 * n-3.......1
    """
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

def factorial_recursion(n):
    """
    parameter : n
    return : n * n-1 * n-2 * n-3.......1
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursion(n-1)

def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


number = int(input("Enter a number"))
print("Factorial using itertaion",factorial_iterative(number))
print("Factorial using recursion",factorial_recursion(number))
print("Fibonacci",fibonacci(number))

