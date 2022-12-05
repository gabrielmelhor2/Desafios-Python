"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hours = int(input("Informe as horas: "))
minutes = input("Informe os minutos: ")
hours_text_morning = "Bom dia, agora são: "
hours_text_afternoon = "Boa tarde, agora são: "
hours_text_night = "Boa noite, agora são: "

if hours >= 0 and hours <= 11:
    print(f"{hours_text_morning}{hours}:{minutes}")
elif hours >= 12 and hours <= 17:
    print(f"{hours_text_afternoon}{hours}:{minutes}")
elif hours >= 18 and hours <= 23:
    print(f"{hours_text_night}{hours}:{minutes}")