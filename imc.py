#Título do programa
print("^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("  WELCOME TO IMC PROGRAM  ")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^")

#Entrada de valores
w = float(input('Your Weight: '))
h = float(input('Your Height: '))
imc = w/(h*h)

#Saída de Valores
if imc > 40:
    print(imc)
    print('Obesity III')
elif imc >= 29.9:
    print(imc)
    print('Obesity I')
elif imc >= 25.9:
    print(imc)
    print('Overweight')
elif imc >= 18.6:
    print(imc)
    print('Normal Weight')
else:
    print(imc)
    print('Underweight')
