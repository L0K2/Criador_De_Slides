from PySimpleGUI import PySimpleGUI as sg
import CriadorDeSlides as t
import Agregar as a
class Gui:

    # Layout
    sg.theme('Reddit')
    layout = [
        [sg.Text("Título"), sg.Input(key="titulo"), sg.Text('',key="mensagem",text_color="red")],
        [sg.Text("Subtítulo"), sg.Input(key="sub")],
        [sg.Text("Insira o texto"), sg.Multiline(s=(100, 10), key="txt")],
        [sg.Button("Enviar")],
        [sg.Text("©Rafael Zorek Soster")]
    ]

    # Janela
    janela = sg.Window("Fazedor de Slide", layout)

    lista = []
    titulo = ""
    sub = ""
    lstCheck = []

    def __init__(self):
        pass

    def run(self):
        while True:
            eventos, valores = Gui.janela.read()
            if eventos == sg.WINDOW_CLOSED:
                break
            if eventos == "Enviar":
                for letter in valores["titulo"]:
                    Gui.lstCheck.append(letter)
                if "." in Gui.lstCheck:
                    Gui.janela["mensagem"].update("O título não pode conter / ou .")
                elif "/" in Gui.lstCheck:
                    Gui.janela["mensagem"].update("O título não pode conter / ou .")
                else:
                    letras = valores["txt"]
                    Gui.sub = valores["sub"]
                    Gui.titulo = valores["titulo"]
                    Gui.lista = letras.split('\n')
                    Gui.lista.append("")
                    #print(Gui.titulo)
                    #print(Gui.lista)
                    #print(a.Agregar.Agregar(a,g.lista))
                    t.CriadorDeSlides.CriaTitulo(t, g.titulo,g.sub)
                    t.CriadorDeSlides.CriaSlideLetra(t, a.Agregar.Agregar(a,g.lista), g.titulo)
                    sg.popup("Slide feito com sucesso!",title="Mensagem")

g = Gui


