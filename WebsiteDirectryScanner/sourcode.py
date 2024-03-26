import tkinter as tk
from tkinter import filedialog
import requests
from urllib.parse import urlparse
import threading

def on_wordlist_entry_select(event):
    wordlist_entry.config(fg=text_color)
    if wordlist_entry.get() == "Select a word list file":
        wordlist_entry.delete(0, tk.END)

def on_url_entry_typing(event):
    if url_entry.get() == "Enter the URL of the website":
        url_entry.delete(0, tk.END)
    url_entry.config(fg=text_color)  

def on_url_entry_paste(event):
    url_entry.config(justify='center')

def normalized_url(url):
    parsed_url = urlparse(url)
    if parsed_url.path.endswith('/'):
        return parsed_url.scheme + '://' + parsed_url.netloc + parsed_url.path[:-1]
    else:
        return url

def scan_website():
    global scan_running
    scan_running = True
    
    def do_scan():
        url = url_entry.get()
        normal_url = normalized_url(url)
        with open(wordlist_entry.get(), 'r') as f:
            for line in f:
                if not scan_running:
                    return  # Stop scanning if stop button is clicked
                word = line.strip()
                full_url = f"{normal_url}/{word}"
                response = requests.get(full_url)
                if response.status_code == 200:
                    output.insert(tk.END, f"Found: {full_url}\n", "found")
                else:
                    output.insert(tk.END, f"Not Found: {full_url}\n", "not_found")
        output.configure(state="disabled") 

    threading.Thread(target=do_scan).start()

def stop_scan():
    global scan_running
    scan_running = False

def toggle_filter():
    if filter_var.get() == 0:
        output.tag_configure("not_found", elide=False)
    else:
        output.tag_configure("not_found", elide=True)

def select_wordlist():
    wordlist_file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if wordlist_file:
        wordlist_entry.delete(0, tk.END)
        wordlist_entry.insert(0, wordlist_file)
        wordlist_entry.event_generate("<FocusIn>")

root = tk.Tk()
root.title("Website Scanner")
root.geometry("400x600")
root.iconbitmap('C:/Users/hidden/Desktop/dp.ico')
root.resizable(False,False)
root.config(bg="#36393f")

accent_color = "#7289da"
button_color = "#4caf50"
text_color = "#ffffff"

url_frame = tk.Frame(root, bg="#36393f")
url_frame.pack(pady=20)

url_entry = tk.Entry(url_frame, width=40, bd=0, bg="#2c2f33", fg="#777777", font=("Arial", 11), justify='center')
url_entry.insert(0, "Enter the URL of the website")
url_entry.pack(side=tk.LEFT, ipady=7, padx=5)
url_entry.bind("<FocusIn>", on_url_entry_typing)

wordlist_frame = tk.Frame(root, bg="#36393f")
wordlist_frame.pack(pady=10)

wordlist_entry = tk.Entry(wordlist_frame, width=36, bd=0, bg="#2c2f33", fg="#777777", font=("Arial", 11), justify='center')
wordlist_entry.insert(0, "Select a word list file")
wordlist_entry.pack(side=tk.LEFT, ipady=7, padx=5)
wordlist_entry.bind("<FocusIn>", on_wordlist_entry_select)

select_wordlist_button = tk.Button(wordlist_frame, text="...", command=select_wordlist, bg=button_color, fg="white", font=("Arial", 11), relief="flat", activebackground=accent_color, activeforeground="white")
select_wordlist_button.pack(side=tk.LEFT, pady=10, padx=5)

output_frame = tk.Frame(root, bg="#36393f")
output_frame.pack(pady=5)

filter_var = tk.IntVar(value=1) 
filter_checkbox = tk.Checkbutton(output_frame, text="Show Found Only", variable=filter_var, command=toggle_filter, bg="#36393f", fg=text_color, selectcolor="#7289da")
filter_checkbox.pack()

output = tk.Text(output_frame, width=50, height=22, bd=0, bg="#2c2f33", fg="#777777", font=("Arial", 10))
output.pack(side=tk.LEFT, padx=20)

output.tag_configure("found", foreground="green")
output.tag_configure("not_found", foreground="red", elide=True)

# Scan button
scan_button = tk.Button(root, text="Scan Website", command=scan_website, bg=button_color, fg="white", font=("Arial", 11), relief="flat", activebackground=accent_color, activeforeground="white", width=12)
scan_button.pack(pady=20, side=tk.LEFT, padx=50)

# Stop button
stop_button = tk.Button(root, text="Stop Scan", command=stop_scan, bg=button_color, fg="white", font=("Arial", 11), relief="flat", activebackground=accent_color, activeforeground="white", width=12)
stop_button.pack(pady=20, side=tk.RIGHT, padx=50)


root.mainloop()
