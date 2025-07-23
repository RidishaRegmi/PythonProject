def write_file(main_data):
    """
    Writes the provided data to database.txt file.

    Parameter:
    main_data: dictionary where keys are IDs and values are list of attributes.

    Exception: If an error occurs, an error message is printed.          
    """
    try:

        #open the file in write mode
        with open("database.txt", "w") as file:

            #iterate over values in dictionary 
            for value in main_data.values():
                #convert each list of attributes to comma separated string
                write_data = str(value[0]) + "," + str(value[1]) + "," + str(value[2]) + "," + str(value[3]) + "\n"
                #write string to file
                file.write(write_data)
    except Exception:
        #print an error msg if writing to file fails
        print("Error writing to file. ")
