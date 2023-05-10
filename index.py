import PySimpleGUI as sg

pizzaList = ["Pepperoni", "Only Cheese", "Spicy", "Vegetarian"]
sizeList = ["Small", "Medium", "Large"]
extraToppings = ["Pepperoni", "Cheese", "Jalepenos"]
sideOrders = []

sg.set_options(font=("Comic Sans", 16))

layout = [ [sg.Text("Your Way Pizza Parlour Order Menu")],
          [sg.Text("What type of Pizza would you like?"), sg.Combo(pizzaList)],
          [sg.Text("What size Pizza would you like?"), sg.Combo(sizeList)],
          [sg.Text("Anything Extra?"), sg.Radio("Yes", "extra", default=False, key="extra"), sg.Radio("No", "extra", default=True)],
          [sg.Button("OK"), sg.Button("Cancel")],
          [sg.Output(size=(40, 10))] ]

window = sg.Window("Your Way Pizza Parlour", layout)

while True:
    event, values = window.read()

    if event == "Cancel" or event == sg.WIN_CLOSED:
        break
    if values["extra"]==True:
        print("Extra Toppings")
    print("You ordered a {size} {type} pizza".format(size=values[0], type=values[1]))

window.close()