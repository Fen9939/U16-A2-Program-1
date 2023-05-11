import PySimpleGUI as sg

class Pizzas:
    def __init__(self, type, size):
        self.__type = type
        self.__size = size

    def getType(self):
        return self.__type
    
    def getSize(self):
        return self.__size
    
class Prices(Pizzas):
    def __init__(self, type, size, price):
        super().__init__(type, size)
        self.__price = price

    def getPrice(self):
        small = 0.85
        medium = 1.0
        large = 1.15
        basePrice = 7.00


    
pizzaOne = Prices("Pepperoni", "£3.12")
pizzaTwo = Prices("Only Cheese", "£.29")
pizzaThree = Prices("Spicy", "£3.29")
pizzafour = Prices("Meaty", "£3.59")
pizzafive = Prices("Vegetarian", "£4.59")

pizzaList = ["Pepperoni", "Only Cheese", "Spicy", "Vegetarian"]
sizeList = ["Small", "Medium", "Large"]

sg.set_options(font=("Comic Sans", 16))
sg.theme('Dark Blue 3')

layout = [ [sg.Text("Your Way Pizza Parlour Order Menu", font=("Comic Sans", 20))],
          [sg.Text("What type of Pizza would you like?"), sg.Combo(pizzaList, default_value="Pepperoni")],
          [sg.Text("What size Pizza would you like?"), sg.Combo(sizeList, default_value="Medium")],
          [sg.Text("Any Extra Toppings?")],
          [sg.Checkbox(f"{pizzaOne.getPrice()} - {pizzaOne.getType()}", key="pep")],
          [sg.Checkbox("Cheese", key="che")],
          [sg.Checkbox("Jalepenos", key="jal")],
          [sg.Checkbox("Sausage", key="sau")],
          [sg.Text("Any Side Orders?")],
          [sg.Checkbox("Garlic Herb Dip", key="pep")],
          [sg.Checkbox("Coleslaw", key="che")],
          [sg.Checkbox("Potato Wedges", key="jal")],
          [sg.Checkbox("Cookies", key="sau")],
          [sg.Button("OK"), sg.Button("Cancel")],
          [sg.Text("")],
          [sg.Text("£" + Prices.getPrice())]
        ]

window = sg.Window("Your Way Pizza Parlour", layout)

while True:
    event, values = window.read()

    if event == "Cancel" or event == sg.WIN_CLOSED:
        break

    print(f"You ordered a {values[1]} {values[0]} pizza")

window.close()