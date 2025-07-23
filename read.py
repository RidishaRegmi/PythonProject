#read_file is a function to read data from file
def read_file():
    """
    Reads the data from file named database.txt.

    Returns a list of strings representing lines from the file.
    """
    try:
        #opening the file in read mode
        with open("database.txt", "r") as file:

            #read lines from file database.txt and returning as list
            file_data = file.readlines()
            return file_data
        
    except FileNotFoundError:

        #print error msg when file is not found.
        print("The database file is missing.")
        return []

def dict(file_content):
    """
    Converts the file content into a dictionary format.

    Parameter:
    file_content: list of strings where each string is a line from file.

    Returns a dictionary where keys are IDs and values are list of attributes.
    """

    data_dict = {}

    #iterate through each line of file_content
    for index in range(len(file_content)):

        #removes newline and splits by comma
        data_dict[index + 1] = file_content[index].replace("\n", "").split(",") 
    return data_dict
