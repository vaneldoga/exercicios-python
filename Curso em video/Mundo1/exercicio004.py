"""
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele.
"""

variavel = input('Digite algo: ')

print(f'O tipo primitivo desse valor é: {type(variavel)}')
print(f'''
        Possui apenas espaços? {variavel.isspace()}
        Contém apenas letras do alfabeto (string/texto)? {variavel.isalpha()} 
        Contém apenas números? {variavel.isnumeric()}
        Contém apenas letras e/ou números (alfanumérico)? {variavel.isalnum()}
        Está apenas em maiúsculas? {variavel.isupper()}
        Está apenas em minúsculas? {variavel.islower()}
        Está em formato de título: {variavel.istitle()}
    ''')
