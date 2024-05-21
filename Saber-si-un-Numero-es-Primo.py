def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

num = int(input("Ingrese un número: "))
print(es_primo(num))