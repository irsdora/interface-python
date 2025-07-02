import PySimpleGUI as sg

class TelaPython
def __init__(self):

    #layout
    layout = [
        [sg.Text('Nome', size=(8,0)), sg.Input(size=(15,0),key='nome')],
        [sg.Text('Estado Civil', size=(8,0)), sg.Input(size=(15,0)key='estadocivil')],
        [sg.Text('Idade', size=(8,0)),sg.Input((15,0),key='idade')],
        [sg.Text('Endereço',size=(8,0)),sg.Input((50,0),  key='endereço')],
        [sg.Text('Quais provedores de e-mail são aceitos?')],
        [sg.Checkbox('Gmail',key='gmail'),sg.Checkbox('Yahoo', key='yahjoo'),sg.Checkbox('Outlook') ],
        [sg.Button('Enviar dados')],
    ]
    #Janela
    janela = sg.Window("Dados do Usuário").layout(layout)
    #Extrair os dados da tela
    self.button, self,values = janela.Read()

    def Iniciar(self):
        nome = self.values['nome']
        estadocivil = self.values['estadocivil']
        idade = self.values['idade']
        endereço = self.values['enedereço']
        aceita_gmail = self.values['gmail']
        aceita_yahoo = self.values['yahoo']
        aceita_outlook = self.values ['outlook']
        print(f'nome:{nome}')
        print(f'idade:{idade}')
        print(f'aceita gmail: {aceita_gmail}')
        print(f'aceita yahoo: {aceita_yahoo}')
        print(f'aceita outlook: {aceita_outlook}')
        



        tela = TelaPython()
        tela.Iniciar()