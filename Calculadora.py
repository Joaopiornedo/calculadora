#Saudação
print("Calculadora Simples: ")
#Operadores
operadores = "1 = Adição 2 = Subtração 3 = Multiplicação 4 = Divisão" 
#criei a função que basicamente é toda calculadora/ ela vai girar até a pessoa dizer que não quer mais calcular:

def calculo ():
        #Pegar numeros / operadores :
        numero1 = int(input("Escolha o primeiro número:"))
        numero2 = int(input("Escolha o segundo número:"))
        print(operadores)

        #inicio conta:

        escolha_cliente = int(input("Digite um operador: "))
        if escolha_cliente == 1:
            print(f"O resultado de sua conta é: {numero1 + numero2}")

        elif escolha_cliente == 2:
            print(f"O resultado de sua conta é: {numero1 - numero2}")

        elif escolha_cliente == 3:
            print(f"O resultado de sua conta é: {numero1 * numero2}")

        elif escolha_cliente == 4:
            print(f"O resultado de sua conta é: {numero1 / numero2}")

        else:        
            print("Operador inválido!")
            
        continuar_conta = str(input("Deseja fazer outra conta ? (s)sim ou (n)não ")).lower()
        if continuar_conta == "s":
            calculo()
        else:
             print("Espero ter ajudado! ")   
#Chamar a função pra rodar :
calculo()





