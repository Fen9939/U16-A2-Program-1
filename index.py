import PySimpleGUI as sg

pizzaList = ["Pepperoni", "Only Cheese", "Spicy", "Vegetarian"]
sizeList = ["Small", "Medium", "Large"]

layout = [ [sg.Text("Your Way Pizza Parlour Order Menu")],
          [sg.Text("What type of Pizza would you like?"), sg.Cobmo(pizzaList)],
          [sg.Text("What size Pizza would you like?"), sg.Combo(sizeList)],
          [sg.Button("OK"), sg.Button("Cancel")] ]

window = sg.Window("Your Way Pizza Parlour", layout)

while True:
    event, values = window.read()

    if event == "Cancel" or event == sg.WIN_CLOSED:
        break
    print("You ordered a {size} {type} pizza".format(size=values[0], type=values[1]))

window.close()