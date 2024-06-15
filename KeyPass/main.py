import tkinter as tk
import os
from tkinter import filedialog

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
            print(" Exiting the program. Goodbye!")
            break
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
    db_name = input("   Enter the name of your database: ")
    master_password = input("   Enter the master password for your database: ")
    documents_folder = os.path.expanduser("~/Documents")
    file_path = os.path.join(documents_folder, f"{db_name}.txt")
    with open(file_path, "w") as file:
        file.write("\n")
    options()

def manage_database():
    banner()
    print(f"\n    Database file '{db_name}' selected in '{file_path}'. \n")
    print(f"    Now handling the database '{db_name}' \n")
    input("    Press enter to continue...")
    options()

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
        print("Exiting the database management system.")
    else:
        print("Invalid choice. Please enter a number from 0 to 4.")

def view_entries(file_path):
    banner()
    with open(file_path, 'r') as file:
        print(file.read())
    input("     Press enter to continue....")
    options()

def create_entry(file_path):
    banner()
    title = input("\n Enter the name of the entry: ")
    uname = input("\n Enter the username / email: ")
    passwd = input("\n Enter the password: ")

    with open(file_path, "a") as file:
        file.write(f"{title}\t{uname}\t{passwd}\n")
        print("Entry added successfully.")
    
    input("Press enter to continue..")
    options()

def edit_entry():
    print("Enter the index of your entry")
    print("Feature not implemented yet....")

def delete_entry():
    print("Enter the index of the entry")
    print("Feature not implemented yet...")

if __name__ == "__main__":
    banner()
    main_menu()
