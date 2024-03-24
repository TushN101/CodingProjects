import tkinter as tk

from tkinter import filedialog

def on_wordlist_entry_focus_in(event):
    if wordlist_entry.get() == "Select a word list file":
        wordlist_entry.delete(0, tk.END)
        wordlist_entry.config(fg=text_color, justify='left')

def on_wordlist_entry_focus_out(event):
    if not wordlist_entry.get():
        wordlist_entry.insert(0, "Select a word list file")
        wordlist_entry.config(fg="#777777", justify='center') 

def on_url_entry_focus_in(event):
    if url_entry.get() == "Enter the URL of the website":
        url_entry.delete(0, tk.END)
        url_entry.config(fg=text_color, justify='left')

def on_url_entry_focus_out(event):
    if not url_entry.get():
        url_entry.insert(0, "Enter the URL of the website")
        url_entry.config(fg="#777777", justify='center') 

def on_wordlist_entry_select(event):
    wordlist_entry.config(fg=text_color)

def on_url_entry_paste(event):
    url_entry.config(justify='center')  

def scan_website():
    url = url_entry.get()
    print("Scanning website:", url)

def select_wordlist():
    wordlist_file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if wordlist_file:
        wordlist_entry.delete(0, tk.END)
        wordlist_entry.insert(0, wordlist_file.split("/")[-1])
        wordlist_entry.event_generate("<FocusIn>")  


root = tk.Tk()
root.title("Website Scanner")
root.iconbitmap(r'C:\Users\hidden\Desktop\dp.ico')  
root.geometry("400x600")
root.resizable(False, False)
root.config(bg="#36393f")


accent_color = "#7289da"
button_color = "#4caf50"
text_color = "#ffffff"


url_frame = tk.Frame(root, bg="#36393f")
url_frame.pack(pady=20)


url_entry = tk.Entry(url_frame, width=40, bd=0, bg="#2c2f33", fg="#777777", font=("Arial", 11), justify='center')
url_entry.insert(0, "Enter the URL of the website") 
url_entry.bind("<FocusIn>", on_url_entry_focus_in)
url_entry.bind("<FocusOut>", on_url_entry_focus_out)
url_entry.bind("<Control-v>", on_url_entry_paste) 
url_entry.pack(side=tk.LEFT, ipady=7, padx=5) 


wordlist_frame = tk.Frame(root, bg="#36393f")
wordlist_frame.pack(pady=10)


wordlist_entry = tk.Entry(wordlist_frame, width=25, bd=0, bg="#2c2f33", fg="#777777", font=("Arial", 11), justify='center')
wordlist_entry.insert(0, "Select a word list file") 
wordlist_entry.bind("<FocusIn>", on_wordlist_entry_focus_in)
wordlist_entry.bind("<FocusOut>", on_wordlist_entry_focus_out)
wordlist_entry.bind("<FocusIn>", on_wordlist_entry_select)
wordlist_entry.pack(side=tk.LEFT, ipady=7, padx=5) 


select_wordlist_button = tk.Button(wordlist_frame, text="...", command=select_wordlist, bg=button_color, fg="white", font=("Arial", 11), relief="flat", activebackground=accent_color, activeforeground="white")
select_wordlist_button.pack(side=tk.LEFT, pady=10, padx=5)


scan_button = tk.Button(root, text="Scan Website", command=scan_website, bg=button_color, fg="white", font=("Arial", 11), relief="flat", activebackground=accent_color, activeforeground="white")
scan_button.pack(pady=10)


root.mainloop()