from datetime import datetime
from read import read_file, dict
from write import write_file

def date_time():
    """
    Gets the current date and time.

    Returns:
    datetime: The current date and time.
    """
    return datetime.now()

def f_print(file_content, main_data):
    """
    Print the furniture data in a tabular format.

    Parameters:
    file_content (list): The content read from the file.
    main_data (dict): A dictionary containing furniture data.

    """
    print("---------------------------------------------------------------------------")
    print("SNo", "\t", "Manufacturer", "\t", "Product", "\t", "Quantity", "\t", "Price")
    print("---------------------------------------------------------------------------")
    for key, value in main_data.items(): 
        print(key, "\t", value[0], "\t", value[1], "\t", value[2], "\t", value[3])
    print("---------------------------------------------------------------------------")
    print("\n") 

def purchase():
    """
    Handle the process of purchasing furniture including updating the database and generating an invoice.

    """
    print("\n")
    print("Purchasing furniture.")
    
    file_content = read_file()
    main_data = dict(file_content)

    furniture = []
    
    while True:
        f_print(file_content, main_data)
        
        #getting item ID from the user
        while True:
            try:
                ID_p = int(input("Enter the ID of the item you want to purchase: "))
                if 0 < ID_p <= len(main_data):
                    break  #exit loop when id valid
                else:
                    print("Enter a valid ID!")
            except ValueError:
                print("Enter a valid number!")
        
        #getting quantity from the user
        while True:
            try:
                quantity_p = int(input("Enter quantity of items you want to purchase: "))
                if quantity_p > 0:
                    break  #exit loop when valid
                else:
                    print("Enter a valid quantity!")
            except ValueError:
                print("Enter a valid number!")

        #updating the main_data with purchase
        main_data[ID_p][2] = str(int(main_data[ID_p][2]) + quantity_p)
        furniture.append([ID_p, quantity_p])

        #write the updated data to the file
        write_file(main_data)
        f_print(file_content, main_data)

        #check if the user wants to purchase more
        user_input = input("Do you want to purchase more furniture? (yes/no): ")
        if user_input.lower() in ["no", "n"]:
            break
        elif user_input.lower() in ["yes", "y"]:
            continue
        else:
            print("Invalid input.")

    #print invoice
    f_print(file_content, main_data)
    p_invoice(furniture)
    print("------------------------------------------------")
    print(" Thank you, the furniture has been purchased!")
    print("------------------------------------------------")


def p_invoice(furniture):
    """
    Generate and print an invoice for the purchased furniture, and save it to a file.

    Parameters:
    furniture (list): A list of lists where each sublist contains an ID and quantity of purchased items.
    """  
    file_content = read_file()
    main_data = dict(file_content)

    employee_name = input("Enter the name of the employee: ")

    print("\n  INVOICE")
    print("\n" + "Employee Name: " + employee_name)
    date = date_time()
    print("Purchase Date: " + str(date))
    print("----------------------------------------------------------------------")
    print("SNo", "\t", "Manufacturer", "\t","Product","\t","Quantity","\t","Price")
    print("----------------------------------------------------------------------")

    #initializing
    total_quantity = 0
    total_price = 0

    for index in range(len(furniture)):
        Id = int(furniture[index][0])
        Quantity = int(furniture[index][1])
        Manufacturer = main_data[Id][0]
        Product = main_data[Id][1]
        Price = int(main_data[Id][3].replace("$", ""))
        
        total_quantity += Quantity
        total_price += Price * Quantity

        print(str(index + 1) , "\t" , Manufacturer , "\t" , Product , "\t" , str(Quantity) , "\t" , str(Price))
        print("\n")
        
    print("------------------------------------------------")
    print("Total Quantity: " + str(total_quantity))
    print("Total Price: $" + str(total_price))
    print("------------------------------------------------")

    #write the invoice to file
    with open(employee_name + ".txt" , "w") as r:
        r.write("\n      INVOICE                     \n")
        r.write("\n" + "Employee Name: " + employee_name + "\n")
        r.write("Purchase Date: " + str(date) + "\n")
        r.write("------------------------------------------------\n")
        r.write("SNo\tManufacturer\tProduct\tQuantity\tPrice\n")
        r.write("------------------------------------------------\n")

        for index in range(len(furniture)):
            Id = int(furniture[index][0])
            Quantity = int(furniture[index][1])
            Manufacturer = main_data[Id][0]
            Product = main_data[Id][1]
            Price = int(main_data[Id][3].replace("$", ""))

            r.write(str(index + 1) + "\t" + Manufacturer + "\t" + Product + "\t" + str(Quantity) + "\t" + str(Price) + "\n")

        r.write("------------------------------------------------\n")
        r.write("Total Quantity: " + str(total_quantity) + "\n")
        r.write("Total Price: $" + str(total_price) + "\n")
        r.write("------------------------------------------------\n")
        r.write("            Thank you for your purchase!      \n")
        r.write("------------------------------------------------\n")

def sell():
    """
    Handle the process of selling furniture including updating the database and generating an invoice.

    """
    print("\n")
    print("Selling furniture.")

    file_content = read_file()
    main_data = dict(file_content)

    furniture = []

    while True:
        f_print(file_content, main_data)
        
        #getting item ID from the user
        while True:
            try:
                ID_s = int(input("Enter the ID of the furniture you want to sell: "))
                if 0 < ID_s <= len(main_data):
                    break  #exit loop if valid ID
                else:
                    print("Enter a valid ID!")
            except ValueError:
                print("Enter a valid number!")

        #getting quantity from the user
        while True:
            try:
                quantity_s = int(input("Enter the quantity of furniture you want to sell: "))
                if 0 < quantity_s <= int(main_data[ID_s][2]):
                    break  #exit loop if valid quantity
                else:
                    print("Not available!")
            except ValueError:
                print("Enter a valid number!")

        #updating the main_data with the sale
        main_data[ID_s][2] = str(int(main_data[ID_s][2]) - quantity_s)
        furniture.append([ID_s, quantity_s])

        #write updated data to the file
        write_file(main_data)
        f_print(file_content, main_data)

        #check if the user wants to sell more items
        user_input = input("Do you want to sell more furniture? (yes/no): ")
        if user_input.lower() in ["no", "n"]:
            break
        elif user_input.lower() in ["yes", "y"]:
            continue
        else:
            print("Invalid input.")

    #print invoice
    f_print(file_content, main_data)
    s_invoice(furniture)
    print("------------------------------------------------")
    print("     Thank you, the furniture has been sold!")
    print("------------------------------------------------")


def s_invoice(furniture):
    """
    Generate and print an invoice for the sold furniture, and save it to a file.

    Parameters:
    furniture (list): A list of lists where each sublist contains an ID and quantity of sold items.

    """
    
    file_content = read_file()
    main_data = dict(file_content)

    user_name = input("Enter your name: ")

    print("\n  INVOICE")
    print("\n" + "Name: " + user_name)
    date = date_time()
    print("Sell Date: " + str(date))
    print("---------------------------------------------------------------")
    print("SNo", "\t", "Brand", "\t","Product","\t","Quantity","\t","Price")
    print("---------------------------------------------------------------")

    #initializing
    total = 0
    for index in range(len(furniture)):
        Id = int(furniture[index][0])
        Quantity = int(furniture[index][1])
        Brand = main_data[Id][0]
        Product = main_data[Id][1]
        Price = int(main_data[Id][3].replace("$", "")) * Quantity

        total += Price

        print(str(index + 1), "\t", Brand, "\t", Product, "\t", str(Quantity), "\t", str(Price))
        print("\n")

    #calculate shipping cost and VAT
    shipping = input("Do you want the furniture shipped? (yes/no): ").lower()
    shipping_cost = 15 if shipping == 'yes' else 0

    vat_rate = 0.13
    vat_amount = total * vat_rate

    #total amount with VAT and shipping cost
    total_with_vat = total + vat_amount
    grand_total = total_with_vat + shipping_cost

    print("------------------------------------------------")
    print("Total price: $" + str(total))
    print("VAT Amount: $" + str(vat_amount))
    print("Shipping cost: $" + str(shipping_cost))
    print("Grand Total: $" + str(grand_total))
    print("------------------------------------------------")

    #write invoice to a file
    with open(user_name + ".txt", "w") as r:
        r.write("\n      INVOICE                     \n")
        r.write("\n" + "Name: " + user_name + "\n")
        r.write("Sell Date: " + str(date) + "\n")
        r.write("------------------------------------------------\n")
        r.write("SNo\tBrand\tProduct\tQuantity\tPrice\n")
        r.write("------------------------------------------------\n")

        for index in range(len(furniture)):
            Id = int(furniture[index][0])
            Quantity = int(furniture[index][1])
            Brand = main_data[Id][0]
            Product = main_data[Id][1]
            Price = int(main_data[Id][3].replace("$", "")) * Quantity

            r.write(str(index + 1) + "\t" + Brand + "\t" + Product + "\t" + str(Quantity) + "\t" + str(Price) + "\n")

        r.write("------------------------------------------------\n")
        r.write("Total price: $" + str(total) + "\n")
        r.write("VAT Amount: $" + str(vat_amount) + "\n")
        r.write("Shipping cost: $" + str(shipping_cost) + "\n")
        r.write("Grand Total: $" + str(grand_total) + "\n")
        r.write("------------------------------------------------\n")
        r.write("             Thank you for your purchase!       \n")
        r.write("------------------------------------------------\n")
