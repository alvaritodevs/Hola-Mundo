def invertir_cadena(cadena):
    return cadena[::-1]

cadena_original = input("Ingresa una palabra: ")
cadena_invertida = invertir_cadena(cadena_original)

print("Cadena original:", cadena_original)
print("Cadena invertida:", cadena_invertida)
