# Imports the `PySimpleGUI` library, which allows for ease when creating GUIs
import PySimpleGUI as sg

# This defines the `Pizzas` class
class Pizzas:
    # This initialises the class
    def __init__(self, type, size, amount):
        self.__type = type
        self.__size = size
        self.__amount = amount

    # This returns the type of pizza
    def getType(self):
        return self.__type
    
    # This returns the size of pizza
    def getSize(self):
        return self.__size
    
    # This returns the amount of pizza
    def getAmount(self):
        return self.__amount

# This defines the `Toppings` class
class Toppings:
    # This initialises the class
    def __init__(self, topping, amount):
        self.__topping = topping
        self.__amount = float(amount)

    # This returns the topping
    def getTopping(self):
        return self.__topping
    
    # This returns the amount of toppings
    def getAmount(self):
        return self.__amount
    
    # This calculates the cost of every selected topping
    def toppCost(self):
        baseCost = 100.0
        tempCost = 0.0
        toppingCost = 0.0

        # This codeblock works out the overall cost of all the selected toppings
        if(self.__topping == "Pepperoni"):
            tempCost = baseCost*self.__amount
            toppingCost = tempCost
        if(self.__topping == "Cheese"):
            tempCost = (baseCost+25)*self.__amount
            toppingCost = toppingCost+tempCost
        if(self.__topping == "Jalepenos"):
            tempCost = (baseCost+25)*self.__amount
            toppingCost = toppingCost+tempCost
        if(self.__topping == "Sausages"):
            tempCost = (baseCost+40)*self.__amount
            toppingCost = toppingCost+tempCost
        
        return toppingCost

# This defines the 'Sides' class
class Sides:
    # This initialises the class
    def __init__(self, side, amount):
        self.__side = side
        self.__amount = float(amount)

    # This defines the 'getSide' function
    def getSide(self):
        return self.__side
    
    # This defines the 'getAmount' function
    def getAmount(self):
        return self.__amount
    
    # This defines the 'sidesCost' function
    def sidesCost(self):
        baseCost = 100.0
        tempCost = 0
        totalCost = 0

        # This codeblock works out the overall cost of all selected side orders
        if(self.__side == "Garlic Herb Dip"):
            tempCost = baseCost*self.__amount
            totalCost = tempCost
        if(self.__side == "Coleslaw"):
            tempCost = (baseCost+15)*self.__amount
            totalCost = totalCost+tempCost
        if(self.__side == "Potato Wedges"):
            tempCost = (baseCost+25)*self.__amount
            totalCost = totalCost+tempCost
        if(self.__side == "Cookies"):
            tempCost = (baseCost+25)*self.__amount
            totalCost = totalCost+tempCost

        return totalCost

# This defines the 'Prices' class
class Prices(Pizzas, Toppings, Sides):
    # This initialises the class
    def __init__(self,  price):
        super(Pizzas).__init__
        super(Toppings).__init__
        super(Sides).__init__
        self.__price = price    

    # This defines the 'getPrice()' function
    def getPrice(self):
        Small = 0.75
        Medium = 1.00
        Large = 2.00
        XL = 2.75
        basePrice = 800
        finalPrice = 0

        # This codeblock works out the overall cost of the chosen pizza(s)
        if self.getType() == "Only Cheese":
            basePrice = basePrice+29
        if self.getType() == "Spicy":
            basePrice = basePrice+79
        if self.getType() == "Meaty":
            basePrice = basePrice+129
        if self.getType() == "Vegetarian":
            basePrice = basePrice+259
        
        if self.getSize() == "Small":
            finalPrice = basePrice*Small
        if self.getSize() == "Medium":
            finalPrice = basePrice*Medium
        if self.getSize() == "Large":
            finalPrice = basePrice*Large
        if self.getSize() == "Extra Large":
            finalPrice = basePrice*XL

        return finalPrice

# This creates a list of all the avabilable pizzas
pizzaList = ["Pepperoni", "Only Cheese", "Spicy", "Meaty", "Vegetarian"]
# This creates a list of all the available sizes
sizeList = ["Small", "Medium", "Large", "Extra Large"]
# This creates a list containing 0-10
amounts = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

# This sets the font and theme options for the GUI
sg.set_options(font=("Comic Sans", 16))
sg.theme('System Default 1')

# This defines the layout of the ordering GUI
layout = [
          [sg.Text("Your Way Pizza Parlour Order Menu", font=("Comic Sans", 20))],
          [sg.Text("What type of Pizza would you like?"), sg.Combo(pizzaList, default_value="Pepperoni", key="Type")],
          [sg.Text("What size Pizza would you like?"), sg.Combo(sizeList, default_value="Medium", key="Size")],
          [sg.Text("How many Pizzas would you like?"), sg.Spin(amounts, initial_value=1, key="pizzaAmount")],
          [sg.Text("Any Extra Toppings?")],
          [sg.Spin(amounts, key="pep", readonly=True, size=3), sg.Text("Pepperoni")],
          [sg.Spin(amounts, key="che", readonly=True, size=3), sg.Text("Cheese")],
          [sg.Spin(amounts, key="jal", readonly=True, size=3), sg.Text("Jalepenos")],
          [sg.Spin(amounts, key="sau", readonly=True, size=3), sg.Text("Sausages")],
          [sg.Text("Any Side Orders?")],
          [sg.Spin(amounts, key="ghd", readonly=True, size=3), sg.Text("Garlic Herb Dip")],
          [sg.Spin(amounts, key="col", readonly=True, size=3), sg.Text("Coleslaw")],
          [sg.Spin(amounts, key="pot", readonly=True, size=3), sg.Text("Potato Wedges")],
          [sg.Spin(amounts, key="coo", readonly=True, size=3), sg.Text("Cookies")],
          [sg.Button("Submit"), sg.Push(), sg.Button("Close")],
        ]

# This initialises the ordering GUI
window = sg.Window("Your Way Pizza Parlour", layout)

# This defines a function called 'orderBillWindow'
def orderBillWindow(price, toppings, sides, pizzas):
    billCol1 = [
        [sg.Text("Price for One")]
    ]
    billCol2 = [
        [sg.Text("Name")],
    ]
    billCol3 = [
        [sg.Text("Amount")]
    ]

    billCol4 = [
        [sg.Text(f"£{Prices.getPrice(pizzas)/100}")]
    ]
    billCol5 = [
        [sg.Text(f"{pizzas.getSize()} {pizzas.getType()}")]
    ]
    billCol6 = [
        [sg.Text(pizzas.getAmount())]
    ]

    billCol7 = [
        [sg.Text("£1.00")],
        [sg.Text("£1.25")],
        [sg.Text("£1.25")],
        [sg.Text("£1.40")]
    ]
    billCol8 = [
        [sg.Text("Pepperoni")],
        [sg.Text("Cheese")],
        [sg.Text("Jalepenos")],
        [sg.Text("Sausages")]
    ]
    billCol9 = [
        [sg.Text(toppings["Pepperoni"])],
        [sg.Text(toppings["Cheese"])],
        [sg.Text(toppings["Jalepenos"])],
        [sg.Text(toppings["Sausages"])]
    ]

    billCol10 = [
        [sg.Text("£1.00")],
        [sg.Text("£1.15")],
        [sg.Text("£1.15")],
        [sg.Text("£1.25")]
    ]
    billCol11 = [
        [sg.Text("Garlic Herb Dip")],
        [sg.Text("Coleslaw")],
        [sg.Text("Potato Wedges")],
        [sg.Text("Cookies")]
    ]
    billCol12 = [
        [sg.Text(sides["Garlic Herb Dip"])],
        [sg.Text(sides["Coleslaw"])],
        [sg.Text(sides["Potato Wedges"])],
        [sg.Text(sides["Cookies"])]
    ]

    # This defines the layout of the bill GUI
    layout = [
        [sg.Text(f"Your total is: £{price}", font=("Comic Sans", 20, "bold"))],
        [sg.Column(billCol1), sg.Column(billCol2), sg.Column(billCol3)],
        [sg.Text("Pizza and Size", font=("Comic Sons", 16, "underline"))],
        [sg.Column(billCol4), sg.Column(billCol5), sg.Column(billCol6)],
        [sg.Text("Extra Toppings", justification="center", font=("Comic Sons", 16, "underline"))],
        [sg.Column(billCol7), sg.Column(billCol8), sg.Column(billCol9)],
        [sg.Text("Side Orders", justification="center", font=("Comic Sons", 16, "underline"))],
        [sg.Column(billCol10), sg.Column(billCol11), sg.Column(billCol12)],
        [sg.Button("OK")]
    ]

    # This initialises the bill GUI
    window = sg.Window("Order Bill", layout, element_justification="c",)

    # This while true loop checks to see if the user presses any buttons
    while True:
        event, values = window.read()

        # This if statement checks to see if the user closes the bill GUI or presses the 'OK' button
        # and then makes a pop up show saying 'Your order has been sent to the kitchen!'
        if event == "OK" or event == sg.WIN_CLOSED:
            sg.popup("Your order has been sent to the kitchen!")
            break

    # This line closes the bill GUI
    window.close()

# This while true loop checks to see if the user presses any buttons
while True:
    event, values = window.read()

    # This if statement checks to see if the use closes the order GUI or presses the 'Close' button
    if event == "Close" or event == sg.WIN_CLOSED:
        break

    # This defines a dictionary containing the extra toppings and amounts of them that the user wants
    toppingsAmounts = {"Pepperoni": values["pep"], "Cheese": values["che"], "Jalepenos": values["jal"], "Sausages": values["sau"]}
    # This defines a dictionary containing the side orders and amounts of them that the user wants
    sidesAmounts = {"Garlic Herb Dip": values["ghd"], "Coleslaw": values["col"], "Potato Wedges": values["pot"], "Cookies": values["coo"]}
    # This initialises a variable called 'totalPrice'
    totalPrice = 0

    # This loops through the 'toppingsAmount' dictionary and works out the price of each topping
    for i in toppingsAmounts:
        tempPrice = Prices.toppCost(Toppings(i, toppingsAmounts[i]))
        totalPrice = totalPrice+tempPrice

    # This loops through the 'sidesAmount' dictionary and works out the price of each side
    for i in sidesAmounts:
        tempPrice = Prices.sidesCost(Sides(i, sidesAmounts[i]))
        totalPrice = totalPrice+tempPrice

    # This works out the price of the pizza based on the type, size, and the amount of them the customer wants
    price = Pizzas(values["Type"], values["Size"], values["pizzaAmount"])
    # This line of code gets the price of everything added together
    finalPrice = (Prices.getPrice(price)+totalPrice)/100
    # This if statement checks to see if the user presses the 'Submit' button, and then opens the bill GUI
    if event == "Submit":
        orderBillWindow(finalPrice, toppingsAmounts, sidesAmounts, price)

# This closes the order GUI
window.close()