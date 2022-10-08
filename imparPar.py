numero = int(input("Digite um valor (Apenas números positivos): "))
resto = numero % 2


if resto == 0 and numero >= 0:
    print("Número", numero, "é par")
elif numero < 0:
    print("Numero invalidado (Somente número inteiro serão aceitos, exemplo: 1,2,3,4,5")
else:
    print("Número", numero, "é impar")