#printing a welcome note 
print("\nWelcome to my interpretation of SEL1T30 Inventory.py \n")
# =======Imports==========
from tabulate import tabulate

# Creating class Shoe
# This class has a constructor method that initialises  the country, code,
# product, cost and quantity and sets them to the values of the arguments sent
# to this method when initialising an object of Shoe class
# This class has four methods: get cost that will return the cost value, get
# quantity that returns the quantity value, and a string method that returns
# the values of all the initialised attributes as strings inside a list

class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return [self.country, self.code, self.product, self.cost,
                self.quantity]
    
# Shoe list
# Defining an empty list that will be used to store a list of objects
# initialised as instances of class Shoe
shoe_list = []

# Functions outside the class
def read_shoes_data():
    """
    This function reads the shoe inventory from an external file. 
    If the file exists, the function will open it in read mode, read the lines and close the file. 
    If the file contains information, each line will be split and 
    the information will be assigned to variables needed to create an object of the Shoe class. 
    Each object will be appended to the shoe list. 
    If the file is empty, a message will be displayed to the user. 
    If the file does not exist, an error message will be displayed.
    """
    try:
        f = open("inventory.txt", "r")
        contents = f.readlines()
        f.close()

        if len(contents) > 0:
            for line in contents:
                if contents.index(line) > 0:
                    country, code, product, cost, quantity = line.strip().\
                        split(",")
                    line = Shoe(country, code, product, cost, quantity)
                    shoe_list.append(line)
        else:
            print("\n\n No data found in the file!\n Please ensure the file "
                  "you are using is populated with your stock data.")
            exit()

    except FileNotFoundError:
        print(" File not found!\n Please ensure you are using the correct "
              "file that contains your stock data")
        exit()

def capture_shoes():
    """
    This function allows the user to input the attributes needed to create a Shoe object. 
    A while loop is used to check that the user input for cost and quantity is correct. 
    If all the data needed for the attributes is introduced correctly, a Shoe object is created and appended to the shoe list. 
    This information is then appended in the text file (*please see notes at the bottom) and a success message is printed. 
    The loop will break. 
    If the user introduces data that is not valid for cost and quantity, 
    error messages will be displayed and the loop will continue asking the user for input.
    """
    input_country = input("\n Please input the country: ")
    input_code = input(" Please input the code: ")
    input_product = input(" Please input the product: ")
    while True:
        try:
            input_cost = int(input(" Please input the cost: "))
            input_quantity = int(input(" Please input the quantity: "))
            if input_cost <= 0 or input_quantity <= 0:
                print(" Please enter values greater than 0!\n")
                continue
            captured_shoes = Shoe(input_country, input_code, input_product,
                                  str(input_cost), str(input_quantity))
            shoe_list.append(captured_shoes)
            f = open("inventory.txt", "a")
            f.write("\n")
            f.write(",".join(captured_shoes.__str__()))
            print("\n Shoes successfully added to the list!")
            break

        except ValueError:
            print("\n Please ensure you enter whole numbers for cost and "
                  "quantity")
            
def view_all():
    """
    This function will take each object in the shoe list and call the string method for it, 
    then append this information in shoe data list. 
    The information in this shoe data list is then displayed in a table format using the Python tabulate module.
    """
    head = ["Country", "Code", "Product", "Cost", "Quantity"]
    shoe_data_list = []
    for shoe in shoe_list:
        shoe_data_list.append(shoe.__str__())
    print("\n\nHere are all your stock details: ")
    print(tabulate(shoe_data_list, headers=head, tablefmt="grid"))

def re_stock():
    """
    This function will display the item with the lowest current stock in table format and prompt the user for input on the quantity to be added. 
    An infinite while loop is used to check for validity of the stock input. 
    If the input is valid (a positive integer), it will be added to the current stock amount and a success message will be printed before breaking the loop. 
    If the input is invalid, error messages will be displayed and the user prompted again. 
    When the stock is modified, the new information will be updated in the text file.
    """
    quantities_list = []
    for shoe in shoe_list:
        quantity = shoe.get_quantity()
        quantities_list.append(int(quantity))
    min_quantity = min(quantities_list)

    shoes_to_be_restocked = None
    for shoe in shoe_list:
        if shoe.quantity == str(min_quantity):
            shoes_to_be_restocked = shoe.__str__()

    print("\nLowest stock details:")
    head = ["Country", "Code", "Product", "Cost", "Quantity"]
    print(tabulate([shoes_to_be_restocked], headers=head, tablefmt="grid"))

    while True:
        try:
            restock_quantity = int(input("\n Please enter the stock to be "
                                         "added: "))
            if restock_quantity > 0:
                shoes_to_be_restocked[4] = str(restock_quantity + min_quantity)
                print("\n Stock successfully updated!")
                break
            else:
                print(" Please ensure the stock to be added is greater than 0"
                      "")
        except ValueError:
            print(" Invalid entry! Please enter a whole number.")

    f = open("inventory.txt", "r+")
    contents = f.readlines()
    f.close()
    f = open("inventory.txt", "w")
    for line in contents:
        line_list = line.strip().split(",")
        if line_list[:4] == shoes_to_be_restocked[:4]:
            f.write(",".join(shoes_to_be_restocked))
            f.write("\n")
        else:
            f.write(line)
    f.close()

def search_shoe():
    """
    This function will allow user to search for a shoe using a code.
    Uses a while loop to check whether the code inputted by the user is valid
    or not.
    The code will go through each shoe object in the list and check if that
    object's code attribute is the same as the code introduced by the user. If
    this is true, the shoe will be added to the show searched list.
    If the shoe searched list is not empty, the information in it will be
    displayed in a table format and the loop will break.
    If the shoe searched list is empty, it means no shoe with that code has
    been found, so user will have an error message and will be asked to insert
    the code again.
    """
    while True:
        shoe_searched = []
        search_code = input("\n Please enter the shoe code to search: ")
        for shoe in shoe_list:
            if shoe.code == search_code:
                shoe_searched.append(shoe.__str__())

        if len(shoe_searched) > 0:
            print("\nHere are the shoes you are looking for:")
            head = ["Country", "Code", "Product", "Cost", "Quantity"]
            print(tabulate(shoe_searched, headers=head, tablefmt="grid"))
            break
        else:
            print(" Product code not found! Please try again.")


def value_per_item():
    """
    This function will calculate the total stock value for each shoe product in
    stock.
    For each object in the shoe list, the value is calculated as the product
    between the cost and the quantity of that object.
    All the information will be displayed in a user-friendly table format.
    """
    product_value_list = []
    for shoe in shoe_list:
        value = int(shoe.cost) * int(shoe.quantity)
        product_value_list.append([shoe.product, str(value)])

    print("\n\nHere is the total value of each item in stock: ")
    print(tabulate(product_value_list, headers=["Product", "Total Value"],
                   tablefmt="grid"))


def highest_qty():
    """
    This function will find the show object with the highest quantity in stock
    and display the this product as being on sale.
    For each object in the shoe list, we get the quantity and append it to the
    quantities list. The highest quantity will be the max number in the list.
    Looping through all the objects in the shoe list again, the object that is
    found to have the highest quantity calculated above, will be the shoe that
    is displayed as being on sale.
    """
    quantities_list = []
    for shoe in shoe_list:
        quantity = shoe.get_quantity()
        quantities_list.append(int(quantity))
    highest_quantity = max(quantities_list)

    shoes_on_sale = None
    for shoe in shoe_list:
        if shoe.quantity == str(highest_quantity):
            shoes_on_sale = shoe.__str__()

    print("\n\nHere are the shoes currently on SALE:")
    head = ["Country", "Code", "Product", "Cost", "Quantity"]
    print(tabulate([shoes_on_sale], headers=head, tablefmt="grid"))

# ==========Main Menu=============
print("""
                                                      
                      INVENTORY MANAGEMENT SYSTEM - PY Ver1 Beta 2  
                    """)

# An infinite loop is used to continuously display the menu to the user
while True:
    # Clear the shoe list to ensure that data is correct on each iteration
    # Read the data in the file by calling the read shoe data function on each
    # iteration
    shoe_list.clear()
    read_shoes_data()
    # Using try except to ensure that the menu choice that the user in entering
    # is an integer
    try:
        # Print user menu on each iteration
        menu = int(input("""\n
         Please choose one of the following options:
    1 => To view all your stock details
    2 => To search an item by the product code
    3 => To view the total value of each item in your stock
    4 => To view items low on stock and re-stock 
    5 => To view items that are on sale (highest stock products)
    6 => To capture data about an item and add this to your stock list
    0 => To exit the system
        """))

        # If user is choosing option 1, display all the data by calling view_
        # all() function.
        # Else if user is choosing option 2, search for a shoe by the code
        # entered, by calling the search_shoe() function
        # Else if user is choosing option 3, calculate and display the total
        # value for each item by calling the value_per_item() function.
        # Else if user is choosing option 4, update the stock of the product
        # with the lowest stock by calling the re_stock() function
        # Else if user is choosing option 5 display the product on sale by
        # calling the highest_qty() function
        # Else if user is choosing option 6, add a new product to the stock by
        # calling the capture_shoe() function
        # Else if user is choosing option 0, print a goodbye message and exit
        # the program.
        # For any other menu choice, print an error message
        if menu == 1:
            view_all()
        elif menu == 2:
            search_shoe()
        elif menu == 3:
            value_per_item()
        elif menu == 4:
            re_stock()
        elif menu == 5:
            highest_qty()
        elif menu == 6:
            capture_shoes()
        elif menu == 0:
            print("""
                    
                              Thank you           
                    """)
            exit()
        else:
            print("\n Wrong choice, please try again!")

    except ValueError:
        print("\n Please ensure you enter a number from 0 to 6!")


            