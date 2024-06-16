import tkinter as tk
import os
from tkinter import filedialog
from tabulate import tabulate

def banner():
    _ = os.system('cls')
    print("\n") 
    print(r"     _  _________   __     __  ____   _    ____ ____  ")
    print(r"    | |/ / ____\ \ / /    / / |  _ \ / \  / ___/ ___| ")
    print(r"    | ' /|  _|  \ V /    / /  | |_) / _ \ \___ \___ \ ")
    print(r"    | . \| |___  | |    / /   |  __/ ___ \ ___) |__) |")
    print(r"    |_|\_\_____| |_|   /_/    |_| /_/   \_\____/____/ ")
    print("")

def main_menu():
    while True:
        banner()
        print("     ------------------------------------------------ \n")
        print("     1. Open an existing database \n")
        print("     2. Create a new database \n")
        print("     3. Exit \n")
        choice = input("     Enter your choice: ")
        if choice == "1":
            open_existing_database()
        elif choice == "2":
            create_new_database()
        elif choice == "3":
            print("\n     Exiting the program. Goodbye!")
            os._exit(0)
        else:
            print(" Invalid choice. Please enter 1, 2, or 3.")

def open_existing_database():
    root = tk.Tk()
    root.withdraw()
    global db_name , file_path
    file_path = filedialog.askopenfilename(title="Select a database file")
    if file_path:
        db_name = os.path.basename(file_path)
        manage_database()
    else:
        print("No file selected.")

def create_new_database():
    banner()
    global db_name, master_password, documents_folder, file_path
    db_name = input("\n    Enter the name of your database: ")
    master_password = input("\n    Enter the master password for your database: ")
    documents_folder = os.path.expanduser("~/Documents")
    file_path = os.path.join(documents_folder, f"{db_name}.txt")
    with open(file_path, "w") as file:
        file.write("")
    options()

def manage_database():
    banner()
    print(f"\n    Database file '{db_name}' selected in '{file_path}'. \n")
    print(f"    Now handling the database '{db_name}' \n")
    loader()

def options():
    banner()
    print(f"    Handling the database '{db_name}' \n")
    print("     0. View all entries \n")
    print("     1. Create a new entry \n")
    print("     2. Edit an entry \n")
    print("     3. Delete an entry \n")
    print("     4. Exit \n")
    choice = input("    Enter your choice: ")  
    
    if choice == "0":
        view_entries(file_path)        
    elif choice == "1":
        create_entry(file_path)
    elif choice == "2":
        edit_entry()
    elif choice == "3":
        delete_entry()
    elif choice == "4":
        main_menu()
    else:
        print("     Invalid choice. Please enter a number from 0 to 4.")

def view_entries(file_path):
    banner()
    with open(file_path, 'r') as file:
        entries = [line.strip().split("\t") for line in file]
        table = tabulate(entries, headers=["Id", "Title", "Username", "Password"], tablefmt="grid")
        indented_table = "\n".join(["    " + line for line in table.split("\n")])
        print(indented_table)   
    loader()

def create_entry(file_path):
    banner()
    title = input("\n    Enter the name of the entry: ")
    uname = input("\n    Enter the username / email: ")
    passwd = input("\n    Enter the password: ")
    id = get_id()
    with open(file_path, "a") as file:
        file.write(f"  {id}\t{title}\t{uname}\t{passwd}\n")
        print("\n    Entry added successfully.")
    
    loader()

def get_id():
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if lines:
                last_line = lines[-1]
                last_id = int(last_line.strip().split("\t")[0])
                return last_id + 1
            else:
                return 1  # If file is empty, start with ID 1
    else:
        return 1  # If file doesn't exist, start with ID 1


def edit_entry():
    banner()
    
    with open(file_path, 'r') as file:
        entries = [line.strip().split("\t") for line in file]
        table = tabulate(entries, headers=["Id", "Title", "Username", "Password"], tablefmt="grid")
        indented_table = "\n".join(["    " + line for line in table.split("\n")])
        print(indented_table)   

    entry_id = int(input("\n    Enter the ID of the entry you want to edit: "))

    entries = []
    with open(file_path, 'r') as file:
        for line in file:
            entry = line.strip().split("\t")
            entries.append(entry)
    
    entry_found = False
    for entry in entries:
        if int(entry[0]) == entry_id:
            entry_found = True
          
            print(f"\n    Editing Entry ID: {entry[0]}")
            new_title = input("\n    Enter new title(or 0 to keep it same): ")
            new_username = input("\n    Enter new username(or 0 to keep it same): ")
            new_password = input("\n    Enter new password(or 0 to keep it same): ")
            
            if new_title != "0":
                entry[1] = new_title
            if new_username != "0":
                entry[2] = new_username
            if new_password != "0":
                entry[3] = new_password
            
            break
    
    if not entry_found:
        print(f"Entry with ID {entry_id} not found.")
    else:
        # Rewrite the file with updated entries
        with open(file_path, 'w') as file:
            for entry in entries:
                file.write("\t".join(entry) + "\n")
        
        print("\n    Entry updated successfully.")

    loader()


def delete_entry():
    banner()

    with open(file_path, 'r') as file:
        entries = [line.strip().split("\t") for line in file]
        table = tabulate(entries, headers=["Id", "Title", "Username", "Password"], tablefmt="grid")
        indented_table = "\n".join(["    " + line for line in table.split("\n")])
        print(indented_table)   

    entry_id = int(input("\n    Enter the ID of the entry you want to delete: "))
    
    entries = []
    with open(file_path, 'r') as file:
        for line in file:
            entry = line.strip().split("\t")
            entries.append(entry)
    
    entry_found = False
    new_entries = []
    for entry in entries:
        if int(entry[0]) == entry_id:
            entry_found = True
            print(f"\n    Deleting Entry ID: {entry[0]}")
        else:
            new_entries.append(entry)
    
    if not entry_found:
        print(f"\n    Entry with ID {entry_id} not found.")

    else:
        with open(file_path, 'w') as file:
            for idx, entry in enumerate(new_entries, start=1):
                entry[0] = str(idx)  # Update the ID
                file.write("\t".join(entry) + "\n")
        
        print("\n    Entry deleted successfully.")
    
    loader()

def loader():
    input("\n    Press enter to continue...")
    options()


if __name__ == "__main__":
    main_menu()
