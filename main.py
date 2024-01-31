print("Ingresa el texto 1: ")
txt1: str = input()

print("Ingresa el texto 2: ")
txt2: str = input()

pasos = 0
fin = len(txt1)

for i in range(0, fin):
    if txt1[i] == txt2[i]:
        print("Caracter en posicion ", i, " es igual")
    else:
        print("Caracter en posicion ", i, " NO es igual, sumando paso")
        pasos = pasos + 1

print("Numero de pasos (distancia de Hamming): ", pasos)
            