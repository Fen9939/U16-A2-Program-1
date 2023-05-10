import PySimpleGUI as sg

layout = [ [sg.Text("Hello from PySimpleGUI")],
          [sg.Text("What Pizza would you like?"), sg.InputText()],
          [sg.Button("OK")] ]

window = sg.Window("Hello World", layout)

while True:
    event, values = window.read()

    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()