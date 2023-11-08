altura=0
massa=0
imc=0
alvomin=0
alvomax=0
while True:
    print("CALCULADORA DE PESO/MASSA IDEAL CONFORME IMC")
    altura = int(input("Quantos centímetros você tem de altura? "))
    massa = int(input("Quantos quiilogramas você tem de peso/massa? "))
    imc=massa/((altura*altura)/10000)
    alvomin=((altura*altura)*18.5)/10000
    alvomax=((altura*altura)*24.99)/10000
    print("\n####")
    print("Seu IMC é",round(imc,2))
    if imc < 17:
        print("Você está MUITO ABAIXO do peso/massa ideal.\nSeu peso/massa ideal é entre",round(alvomin,2),"e",round(alvomax,2),"quilogramas.")
    elif imc < 18.5:
        print("Você está ABAIXO do peso/massa ideal.\nSeu peso/massa ideal é entre",round(alvomin,2),"e",round(alvomax,2),"quilogramas.")
    elif imc < 25:
        print("Você está com o peso/massa IDEAL.\nSeu peso/massa ideal é entre",round(alvomin,2),"e",round(alvomax,2),"quilogramas.")
    elif imc < 30:
        print("Você está ACIMA do peso/massa ideal.\nSeu peso/massa ideal é entre",round(alvomin,2),"e",round(alvomax,2),"quilogramas.")
    elif imc < 35:
        print("Você está OBESO.\nSeu peso/massa ideal é entre",round(alvomin,2),"e",round(alvomax,2),"quilogramas.")
    elif imc < 40:
        print("Você está em OBESIDADE SEVERA.\nSeu peso/massa ideal é entre",round(alvomin,2),"e",round(alvomax,2),"quilogramas.")
    else:
        print("Você está em OBESIDADE MÓRBIDA.\nSeu peso/massa ideal é entre",round(alvomin,2),"e",round(alvomax,2),"quilogramas.")
    break
print("####")
