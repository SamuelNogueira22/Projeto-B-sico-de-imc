#Crie um programa que solicite ao usuário informações como nome, 
#idade e altura, e utilize essas variáveis para exibir uma mensagem personalizada.

#1º Parte do Código, coleta das informações básicas
nome = str(input("Diga aqui seu nome: "))
idade = int(input("Diga aqui sua idade: "))
altura = float(input("Diga aqui sua altura em metros: "))
peso = float(input("Diga aqui seu peso em Quilos: "))

#Reunindo e organizando as informações
print("Olá, seja bem vindo,",nome,"identificamos aqui que sua idade é",idade, "sua altura é",altura, "e seu peso é",peso)

#2º Parte do código

imc = peso / (altura * altura)
if imc <18.5:
    print("Você está abaixo do peso, IMC: ",f'{imc:.2f}')
elif 18.5 < imc < 24.9:
    print("Seu Peso está normal, IMC: ",f'{imc:.2f}')
elif 25 < imc < 29.9:
    print("Sobrepeso!, IMC: ",f'{imc:.2f}')
elif imc > 30:
    print("Obesidade, IMC: ",f'{imc:.2f}')
else:
    print("Dados inválidos! Favor tente novamente.")

class indicador:
    if 18.5 < imc < 24.9:
        print("Parabéns! Tudo certo contigo.")
    elif imc < 18.5 or 25 < imc < 30:
        print("Tua saúde está em risco! Deves consultar um profissional o mais rápido possível, mais informações em https://www.gov.br/saude/pt-br/assuntos/saude-brasil/eu-quero-ter-peso-saudavel/noticias/2017/imc-voce-sabe-calcular-seu-peso-adequado")
    else:
        print("Dados inválidos! Tente de novo ou se informe melhor em https://www.gov.br/saude/pt-br/assuntos/saude-brasil/eu-quero-ter-peso-saudavel/noticias/2017/imc-voce-sabe-calcular-seu-peso-adequado")


print(nome,"Muito obrigado por utilizar nossos serviços, esperemos que esteja satisfeito -->")