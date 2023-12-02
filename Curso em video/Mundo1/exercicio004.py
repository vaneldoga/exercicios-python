"""
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele.
"""

var = input('Digite algo: ')

print(f'O tipo primitivo desse valor é: {type(var)}')
print(f'''
        Possui apenas espaços? {var.isspace()}
        Contém apenas letras do alfabeto (string/texto)? {var.isalpha()} 
        Contém apenas números? {var.isnumeric()}
        Contém apenas letras e/ou números (alfanumérico)? {var.isalnum()}
        Está apenas em maiúsculas? {var.isupper()}
        Está apenas em minúsculas? {var.islower()}
        Está em formato de título: {var.istitle()}
    ''')
