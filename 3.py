"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Digite seu nome: ")
length_name = len(nome)

if length_name <= 4:
    print("Seu nome é curto")
elif length_name <= 5 and length_name <= 6:
    print("Seu nome é normal")
elif length_name < 6:
    print("Seu nome é muito grande")