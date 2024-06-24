#  Tabuada de Multiplicação

numero = int(input("Digite um número: "))
tabuada = 0

while tabuada <= 10:
    resultado = numero * tabuada
    print(f'A multiplicação de {numero} x {tabuada} é {resultado}')
    tabuada = tabuada + 1