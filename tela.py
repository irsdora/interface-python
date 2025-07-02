import PySimpleGUI as sg

class TelaPython
def __init__(self):
    #layout
    layout = [
        [sg.Text('Nome', size=(8,0)), sg.Input(size=(15,0))],
        [sg.Text('Estado Civil', size=(8,0)), sg.Input(size=(15,0))],
        [sg.Text('Idade', size=(8,0)), sg.Input()],
        [sg.Text('Endereço', size=(8,0)), sg.Input()],
        [sg.Checkbox()],
        [sg.Button()],
        
    ]

    #Janela
