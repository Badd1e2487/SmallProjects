"""
Simple Input Program!
Available Commands: 'name', 'commands', 'help', 'exit'.
"""

print("Input Program! \n")

while True: # For Looping again and again till user stops the program.
    text = input("Enter your command: ")
    
    if text.lower() == "name": # Name Command. These are Nested-If Statements.
        name = input("Enter your name: ")
        question = input("Do you want to enter your surname? Y:Yes - N:No: ")
        
        if question.lower() == "yes":
            surname = input("Enter your surname: ")
            print(f"Your name is {name} {surname}!")
           
        elif question.lower() == "y":
            surname1 = input("Enter your surname: ")
            print(f"Your name is {name} {surname1}!")
            
        elif question.lower() == "n":
            print(f"Your name is {name}!")
            
        elif question.lower() == "no":
            print(f"Your name is {name}!")
            
        else:
            print("Invalid Argument! Try again")
    
    elif text.lower() == "exit": # Exit Command
        print("Succesfully exited the program!")
        break
        
    elif text.lower() == "commands": # Commands Command
        print("Available Commands: 'name', 'exit', 'help'.")
        
    elif text.lower() == "help": # Help Command
        print("Help! \n")
        print("Commands: \n")
        print("Name - Simple Name Input Program.")
        print("Commands - Shows the list of commands available.")
        print("Exit - Exits the program.")
    else:
        print("Invalid Command!")
        print("Type 'help' to know more!")
        
    print("\n")
    exit = input("Do You Want to Continue? Y:Yes - N:No: ") # Do You Want to Continue Dialog.
    if exit.lower() == "no":
        break
    elif exit.lower() == "n":
        break
    elif exit.lower() == "yes":
        continue
    elif exit.lower() == "y":
        continue
        
    # THE END.
