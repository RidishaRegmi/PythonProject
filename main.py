from operation import purchase, sell
from read import read_file, dict
from operation import f_print

def main():
    """
    Provides a menu for the user to view available furniture,
    sell items, purchase items, or exit the program.
    
    """
    print("------------------------------------------------")
    print("************************************************")
    print("          Welcome to BRJ Furnitures             ")
    print("Kamalpokhari, Kathmandu | Contact no.9812345678")
    print("************************************************")
    print("------------------------------------------------")

    loop = True

    while loop:
        print("------------------------------------------------")
        print("Select the preferred option: ")
        print("Press 1 to view available furniture.")
        print("Press 2 to sell the items to the customers.")
        print("Press 3 to purchase from the manufacturers.")
        print("Press 4 to exit from program.")
        print("------------------------------------------------")

        try:
            choose = int(input("Enter your preferred option: "))
        except ValueError:
            print("Enter a valid number: ")
            continue

        if choose == 1:
            #view available furnitures
            file_content = read_file()
            main_data = dict(file_content)
            f_print(file_content, main_data)

        elif choose == 2:
            #sell items to customers
            try:
                sell()
            except Exception:
                print("An error occurred during the process.")

        elif choose == 3:
            #purchase items from manufacturers
            try:
                purchase()
            except Exception:
                print("An error occurred during the process.")

        elif choose == 4:
            #exit the program
            print("Thank you!")
            print("\n")
            loop = False

        else:
            print("Enter a valid number: ")

#run main function to start the program
main()
