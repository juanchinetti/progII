#conversor de moneda

# Tipo de cambio fijo de dólares a euros
tipo_cambio = 0.85  # 1 dólar = 0.85 euros (valor ficticio)

# Solicitar al usuario que ingrese la cantidad en dólares
cantidad_dolares = float(input("Ingrese la cantidad en dólares: "))

# Convertir dólares a euros
cantidad_euros = cantidad_dolares * tipo_cambio

# Mostrar la cantidad equivalente en euros
print("La cantidad equivalente en euros es:", cantidad_euros)