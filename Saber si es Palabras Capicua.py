def capicua(palabra):
    reves = ""
    for i in range(len(palabra)-1, -1, -1):
        reves += palabra[i]

    return palabra == reves

palabra = input("Ingrese una palabra: ")
print(capicua(palabra))