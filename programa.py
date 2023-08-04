# Bibliotecas
from random import randint
from tkinter import Tk, ttk

# Código principal


def gerar():
    # Gerar os 9 primeiros números do CPF aleatoriamente
    gerador_cpf = ''
    for i in range(9):
        gerador_cpf += str(randint(0, 9))

    CPF = gerador_cpf

    # Gerar o primeiro digito do CPF (digitos são os números depois do traço "-")
    CPF_1 = CPF

    mult_1 = 10
    cpf_soma_1 = 0

    # Coletar a soma dos 9 números do CPF multiplicando cada um dos números por uma contagem regressiva começando de 10
    for numero_1 in CPF_1:
        numero_1 = int(numero_1)
        cpf_soma_1 += numero_1 * mult_1
        mult_1 -= 1

    # Multiplicar a soma do resultado anterior por 10
    cpf_vezes_dez_1 = cpf_soma_1 * 10

    # Obter o resto da divisão da conta anterior por 11
    resto_digito_1 = cpf_vezes_dez_1 % 11

    # Validação do primeiro digito do CPF
    if resto_digito_1 > 9:
        primeiro_digito = 0
    else:
        primeiro_digito = resto_digito_1

    # Gerar o segundo digito do CPF (digitos são os números depois do traço "-")
    CPF_2 = f'{CPF_1}{primeiro_digito}'

    mult_2 = 11
    cpf_soma_2 = 0

    # Coletar a soma dos 9 primeiros dígitos do CPF, mais o primeiro digito,
    # multiplicando cada um dos valores por uma contagem regressiva começando de 11
    for numero_2 in CPF_2:
        numero_2 = int(numero_2)
        cpf_soma_2 += numero_2 * mult_2
        mult_2 -= 1

    # Multiplicar a soma do resultado anterior por 10
    cpf_vezes_dez_2 = cpf_soma_2 * 10

    # Obter o resto da divisão da conta anterior por 11
    resto_digito_2 = cpf_vezes_dez_2 % 11

    # Validação do segundo digito do CPF
    if resto_digito_2 > 9:
        segundo_digito = 0
    else:
        segundo_digito = resto_digito_2

    # CPF Válido Gerado
    digitos = f'{primeiro_digito}{segundo_digito}'
    cpf_completo = f'{CPF}{digitos}'

    if cpf_completo[9:] == digitos:
        texto_resposta['text'] = f'{cpf_completo[0:3]}.{cpf_completo[3:6]}.{cpf_completo[6:9]}-{cpf_completo[9:]}'


# Interface Gráfica - GUI
# Janela Principal
root = Tk()

# Título da janela
root.title('Gerador de CPF')

# Widget
botao_gerador = ttk.Button(
    text='GERAR CPF',
    command=gerar
)

# Output Widget
texto_resposta = ttk.Label(
    root,
    text='',
    font=('Arial', 11)
)

# Dimensionamento dos Widgets
botao_gerador.pack(padx=100, pady=10)
texto_resposta.pack(pady=5)

# Mantém a janela principal rodando
root.mainloop()
