def ler_numero_inteiro():
    while True:
        try:
            tamanho_senha = input('Quantos caracteres sua senha deve ter? ')
            
            if not tamanho_senha.isdigit():  
                raise ValueError('A entrada deve conter apenas um número inteiro')

            tamanho_senha = int(tamanho_senha) 

            if not (8 <= tamanho_senha <= 32):  
                raise ValueError('O número deve estar entre 8 e 32.')

            return tamanho_senha
            
        except ValueError as mensagem_erro:
            print(f'Erro: {mensagem_erro}')

def senha_com_numero():
    while True:
        try:
            numero_input = input('Sua senha deve conter números? [S/N] ').strip().upper()

            if numero_input == 'S':
                return True
            if numero_input == 'N':
                return False
            else:
                raise ValueError("Resposta inválida! Por favor, responda com 'S' ou 'N'.")
            
        except ValueError as mensagem_erro:
            print(f'Erro: {mensagem_erro}')

def senha_com_letra():
    while True:
        try:
            letra_input = input('Sua senha deve conter letras? [S/N] ').strip().upper()

            if letra_input == 'S':
                return True
            if letra_input == 'N':
                return False
            else:
                raise ValueError("Resposta inválida! Por favor, responda com 'S' ou 'N'.")
            
        except ValueError as mensagem_erro:
            print(f'Erro: {mensagem_erro}')

def senha_com_letra_maiuscula():
    while True:
        try:
            letra_maiuscula_input = input('Sua senha deve conter letras maiúsculas? [S/N] ').strip().upper()

            if letra_maiuscula_input == 'S':
                return True
            if letra_maiuscula_input == 'N':
                return False
            else:
                raise ValueError("Resposta inválida! Por favor, responda com 'S' ou 'N'.")
            
        except ValueError as mensagem_erro:
            print(f'Erro: {mensagem_erro}')

def senha_com_caracter_especial():
    while True:
        try:
            caracter_especial_input = input('Sua senha deve conter caracter especial? [S/N] ').strip().upper()

            if caracter_especial_input == 'S':
                return True
            if caracter_especial_input == 'N':
                return False
            else:
                raise ValueError("Resposta inválida! Por favor, responda com 'S' ou 'N'.")
            
        except ValueError as mensagem_erro:
            print(f'Erro: {mensagem_erro}')