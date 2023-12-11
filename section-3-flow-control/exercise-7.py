"""
Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas,
pero no debe repetirse ningún elemento en la nueva lista.
"""

lista_1 = ['h','o','l','a',' ','m','u','n','d','o']
lista_2 = ['h','o','l','a',' ','l','u','n','a']
lista_3 = []

# Recorremos la lista_1
for letra in lista_1:
    # Comparamos con la lista_2 y además verificamos que la letra no esté en lista_3
    if letra in lista_2 and letra not in lista_3:
        lista_3.append(letra)

print(lista_3)
