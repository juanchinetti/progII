def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def main():
    n = int(input("Enter a number: "))
    resultado = factorial(n)
    print(f"The factorial of {n} is {resultado}")

main()