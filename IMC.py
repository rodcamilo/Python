altura=0
massa=0
imc=0
while True:
    print("CALCULADORA DE IMC")
    altura = int(input("Quantos centímetros você tem de altura? "))
    massa = int(input("Quantos quiilogramas você tem de peso/massa? "))
    imc=massa/((altura*altura)/10000)
    print("\n####")
    print("Seu IMC é ",round(imc,2))
    if imc < 17:
        print("Você está MUITO ABAIXO do peso/massa ideal. Procure auxílio médico. O IMC saudável é entre 18,5 e 24,99.")
    elif imc < 18.5:
        print("Você está ABAIXO do peso/massa ideal. O IMC saudável é entre 18,5 e 24,99.")
    elif imc < 25:
        print("Você está com o peso/massa IDEAL. O IMC saudável é entre 18,5 e 24,99.")
    elif imc < 30:
        print("Você está ACIMA do peso/massa ideal. O IMC saudável é entre 18,5 e 24,99.")
    elif imc < 35:
        print("Você está OBESO. Procure auxílio médico. O IMC saudável é entre 18,5 e 24,99.")
    elif imc < 40:
        print("Você está em OBESIDADE SEVERA. Procure auxílio médico URGENTE! O IMC ideal é entre 18,5 e 24,99.")
    else:
        print("Você está em OBESIDADE MÓRBIDA. Procure auxílio médico URGENTE! O IMC ideal é entre 18,5 e 24,99.")
    break
print("####")
