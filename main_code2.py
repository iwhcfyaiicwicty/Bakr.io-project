text_name = input("Which text would you like to search (please use .txt format)? ")

while text_name != '':
    types_of_bread = []
    bread = input("Name a type of bread (type 'done' to stop): ")
    while bread != 'done':
        bread = types_of_bread.append(bread)
        bread = input("Name a type of bread (type 'done' to stop): ")

    red = '\033[91m'
    italics = '\033[3m'
    underline = '\033[4m'
    end = '\033[0m'

    with open (text_name, 'r') as text:
        for line in text:
            line = line.strip('\n')
            for type in types_of_bread:
                if type in line: 
                    newline = line.replace(type, red + italics + underline + type + end)
                    print(newline)
                else: 
                    print("...")     
                   
    print('\nSearch is complete!\n' )
    continue_loop = input("Would you like to search another text (yes/no)? ")
    if continue_loop == 'yes':
        text_name = input("Which text would you like to search next (please use .txt format)? ")
    else:
        text_name = ''


print("\nHave an amaize-ing day!\n")
