import PySimpleGUI as sg
from faker import Faker

# Inicializar o Faker com a localidade brasileira
fake = Faker('pt_BR')

# Função para gerar dados
def gerar_dados(values):
    # Função para obter o valor da entrada ou retornar zero se estiver vazio
    def get_input_value(key):
        value = values[key]
        return int(value) if value.isdigit() else 0

    # Obter a quantidade de dados a serem gerados a partir das entradas do usuário
    qtd_nome = get_input_value('-NOME-')
    qtd_endereco = get_input_value('-ENDERECO-')
    qtd_cpf = get_input_value('-CPF-')
    qtd_numeros = get_input_value('-NUMEROS-')

    # Gerar e mostrar os dados
    resultado = ""
    
    for _ in range(qtd_nome):
        nome_completo = fake.name()
        resultado += f"Nome gerado é: {nome_completo}\n\n"
    
    for _ in range(qtd_endereco):
        endereco = fake.address()
        resultado += f"Endereço gerado é: {endereco}\n\n"
    
    for _ in range(qtd_cpf):
        cpf = fake.cpf()
        resultado += f"CPF gerado é: {cpf}\n\n"
    
    for _ in range(qtd_numeros):
        numero = fake.phone_number()
        resultado += f"Numero gerado é: {numero}\n\n"
    
    return resultado

# Definir o tema escuro
sg.theme('DarkGrey13')

# Layout da interface
layout = [
    [sg.Text("Quantos nomes você quer gerar?"), sg.Input(key='-NOME-', size=(5,1))],
    [sg.Text("Quantos endereços você quer gerar?"), sg.Input(key='-ENDERECO-', size=(5,1))],
    [sg.Text("Quantos CPFs você quer gerar?"), sg.Input(key='-CPF-', size=(5,1))],
    [sg.Text("Quantos números de telefone você quer gerar?"), sg.Input(key='-NUMEROS-', size=(5,1))],
    [sg.Button('Gerar Dados')],
    [sg.Multiline(size=(60, 20), key='-OUTPUT-', font=("Helvetica", 12))]
]

# Criar a janela
window = sg.Window("Gerador de Dados", layout, size=(500, 600))

# Loop da interface gráfica
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Gerar Dados':
        resultado = gerar_dados(values)
        window['-OUTPUT-'].update(resultado)

# Fechar a janela
window.close()
