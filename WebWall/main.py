import os
import threading
from tabulate import tabulate

file_path = r'C:\Windows\System32\drivers\etc\hosts'

def print_red_banner(text):
    print('\033[91m' + text + '\033[0m')

def banner():
	_ = os.system('cls')
	print("\n\n")
	print_red_banner(r"	                      d8b                                d8b  d8b    ")
	print_red_banner(r"	                       ?88                               88P  88P   ")
	print_red_banner(r"	                        88b                              d88  d88    ")
	print_red_banner(r"	 ?88   d8P  d8P d8888b  888888b  ?88   d8P  d8P d888b8b  888  888    ")
	print_red_banner(r"	 d88  d8P' d8P'd8b_,dP  88P `?8b d88  d8P' d8P'd8P' ?88  ?88  ?88    ")
	print_red_banner(r"	 ?8b ,88b ,88' 88b     d88,  d88 ?8b ,88b ,88' 88b  ,88b  88b  88b   ")
	print_red_banner(r"	 `?888P'888P'  `?888P'd88'`?88P' `?888P'888P'  `?88P'`88b  88b  88b  ")
	print("\n\n")


def add_websites_to_block():
    banner()
    table()
    redirect = input("\n         Specify redirects (Not needed | Press enter to skip): ")

    if redirect == "":
        redirect = "0.0.0.0"

    while True:
        website = input("\n         Keep entering website domain (or 'done' to finish): ")
        if website.lower() == "done":
            break
        if website != "":
            with open(file_path, 'a') as f:
                f.write(f"{redirect} {website}\n")

    print("\n         WebWall Updated Successfully!")
    input("\n         Press and key to continue...")


def remove_websites_from_block():
    banner()
    table()
    id_to_remove = input("\n         Enter the ID you want to remove: ")

    with open(file_path, 'r') as filedata:
        lines = filedata.readlines()

    with open(file_path, 'w') as filedata:
        for i, line in enumerate(lines, start=1):
            if str(i) != id_to_remove:
                filedata.write(line)

    print("\n         WebWall Removed Successfully!")
    input("\n         Press Enter to continue...")


def view_blocked_websites():
    banner()
    table()
    input("\n         Press and key to continue...")

def table():
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
            data = []
            for i, line in enumerate(lines, start=1):
                redirect, website = line.strip().split()
                data.append([i, website, redirect])
            table_str = tabulate(data, headers=['ID', 'Website', 'Redirect'], tablefmt='grid')
            indented_table_str = "\n".join("         " + line for line in table_str.split("\n"))
            print(indented_table_str)
    except FileNotFoundError:
        print(f"Failed to Initiate table")


def clean():
    try:
        with open(file_path, 'r+') as f:
            f.truncate(0)
    except:
        print("There was a error | Program wont work")

def main():
    while True:
        banner()
        print("\n         1. View Blocked Websites\n")
        print("         2. Add Websites to Block\n")
        print("         3. Remove Websites from Block\n")
        print("         4. Exit\n")
        
        choice = input("         Enter your choice: ")
        
        if choice == "1":
            view_blocked_websites()
        elif choice == "2":
            add_websites_to_block()
        elif choice == "3":
            remove_websites_from_block()
        elif choice == "4":
            print("\n     Exiting the program. Goodbye!\n")
            clean() 
            break  
        else:
            print("\n     Invalid choice. Please enter a number from 1 to 4.")


if __name__ == '__main__':
    clean()
    main()                                             
            
