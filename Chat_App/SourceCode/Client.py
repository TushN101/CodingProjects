#importing required modules
import socket #importing the socket module necessary for networking tasks 
import threading #importing the threading module helps to run multiple multiple threads
import tkinter as tk #importing the tkinter module for gui as tk
from tkinter import scrolledtext #importing the scrolledtext module from the tkinter package, allowing direct use of the scrolledtext 
from tkinter import messagebox #imports the messagebox module from the tkinter package


HOST = '127.0.0.1' #Setting the hosts the client will connect to
PORT = 1234 #Setting the port anything other than the general ports that are being used to which the client will connect to
username = ""
DARK_GREY = '#121212' #Regulatory things for the GUI
MEDIUM_GREY = '#1F1B24' #Regulatory things for the GUI
OCEAN_BLUE = '#464EB8'  #Regulatory things for the GUI
WHITE = "white" #Regulatory things for the GUI
FONT = ("Helvetica", 13)    #Regulatory things for the GUI
SMALL_FONT = ("Helvetica", 13)  #Regulatory things for the GUI

#Creating a socket called client for network communication using IPv4 addressing and communication through the TCP protocol.
client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

#Setting the function that updates a Tkinter Text widget message_box by adding a new message at the end (i.e end of previous text)
def add_message(message):
    message_box.config(state=tk.NORMAL) #Setting the config of the message box to normal so that we can add the text 
    message_box.insert(tk.END, message + '\n') #Adding the text at the end that is at the end of last statement and then add new line so that yk better
    message_box.config(state=tk.DISABLED) #Setting the config of the message box to disabled so that no further addiion of text directly from the client 

#Setting the function that gets triggered when user clicks on the join option
def connect():
    try: #Trying to connecting to the server
        client.connect((HOST,PORT)) #Establishes a connection from a client socket (client) to a specified server address (HOST and PORT).
        print(f"Succesfully connected to the server {HOST} {PORT}") #Displaying that the connnection was succesfull
        add_message("[SERVER] Succesfully connected to the Server") #Displaying that message on the message box by calling the function that puts mssg on mssg box 
    except: #Except thing to do if not able to connect 
        messagebox.showerror("Unable to connect to server", f"Unable to connect to the server {HOST} {PORT}")
        #messagebox.showerror is used to create a new window titled as the first argument and showing the error as in the second argument 
    
    #Thing to do after the connnection with the server was succesfull
    username = username_textbox.get() #Getting the text from the username coloumn that was entered before pressing join 
    if username != ' ': #If the username box was not empty  
       client.sendall(username.encode()) #Then send the username and encode it and it is recieved by  client handler function on the server side code 
    else: #Else if the username box was empty 
        messagebox.showerror("Invalid username detected","Username cant be empty") #Create a new windows that throws a error with that title and that error content 
        exit(0) #Exit  
    
    threading.Thread(target=listen_for_message_from_server, args=(client,)).start() #Threading it so that it runs parallely and doing the thingy of getting mssg from other clients
    #threading to make sure that it runs parallely without hindering in the main program 
    
    username_textbox.config(state=tk.DISABLED) #After connection disabling the client from entering anything into the client text box 
    username_button.config(state=tk.DISABLED) #After connection disablinig the client from pressing the join button again
    
#Setting the command that will be triggered when the send button is pressed 
def send_message(): 
    message = message_textbox.get() #This will get the things that was typed into the message text box 
    if message != '' : #If the message was not empty 
        client.sendall(message.encode()) #Send the message to all and encode  it before sending 
        message_textbox.delete(0,len(message)) #Starting zero index to the length of messsage deleted so that empty space for new text
    else: #If the message was empty 
        message_box.showerror("Message box error","Message cannot be empty") #Create a new wimdow and show the error title and the content 


root = tk.Tk() #used to create the main window or the root window
root.geometry("600x600") #Setting the dimension of the window that will be created 
root.title("Messenger Client") #Setting the title that the window will have
root.resizable(False,False) #First argument for false for width second argument false for height change 

#Specifying height to rows assign 
root.grid_rowconfigure(0, weight=1) #Assigning the first row indexed zero and weight(height=100)
root.grid_rowconfigure(1, weight=4) #Assigning the second row indexed one and weight(height=400)
root.grid_rowconfigure(2, weight=1) #Assigning the third row indexed two and weight(height=100)

top_frame = tk.Frame(root, width=600 , height = 100 , bg = DARK_GREY) #Setting the height and the width of the top frame and setting its bg colour in the root window 
top_frame.grid(row = 0 , column=0 , sticky=tk.NSEW) #tk.NSEW means the widget expands in all directions (North, South, East, West), filling the entire cell
#Giving the top frame the first row that is indexed at zero 

middle_frame = tk.Frame(root, width=600 , height = 400 , bg = MEDIUM_GREY) #Setting the height and width of the middle frame and setting its bg colour in the root window 
middle_frame.grid(row = 1 , column=0 , sticky=tk.NSEW) #tk.NSEW means the widget expands in all directions (North, South, East, West), filling the entire cell
#Giving the middle frame the first row that is indexed at one

bottom_frame = tk.Frame(root, width=600 , height = 100 , bg = DARK_GREY) #Setting the height and width of the bottom frame and setting its bg colour in the root window 
bottom_frame.grid(row=2,column=0,sticky=tk.NSEW) #tk.NSEW means the widget expands in all directions (North, South, East, West), filling the entire cell
#Giving the bottom frame the third row indexed at two 

username_label = tk.Label(top_frame , text="Enter username" , font=FONT , bg=DARK_GREY , fg=WHITE) #Creating a label text of username in the top frame at the left
username_label.pack(side=tk.LEFT , padx=10) #.pack() is used to place the widget from the left of the top frame container and padding is the extra more spacing given

username_textbox = tk.Entry(top_frame, font=FONT, bg=MEDIUM_GREY , fg=WHITE , width=34) #Creating a textbox in where we will type the username 
username_textbox.pack(side=tk.LEFT) #.pack() is used to place the widget from the left of the top frame container and no padding is given

username_button = tk.Button(top_frame, text="JOIN", font=FONT, bg=OCEAN_BLUE, command=connect) #Creating a button with the text JOin and the command i.e the function it will trigger
username_button.pack(side=tk.LEFT, padx=15) #.pack() is used to place the widget from the left of the top frame container and padding is the extra spacing given

message_textbox = tk.Entry(bottom_frame, font=FONT, bg=MEDIUM_GREY ,fg=WHITE, width=57) #Creatinga a message box in the bottom frame where client will type the message
message_textbox.pack(side=tk.LEFT, padx=10) #.pack() is used to place the widget from the left of the middle frame with extra paddinng of 10px

message_button = tk.Button(bottom_frame,text="Send" , font=FONT , bg=OCEAN_BLUE , fg=WHITE , command=send_message) #Creating a button with text SEND and a function send message that it will trigger
message_button.pack(side=tk.LEFT) #.pack() is used to place that widget from the left of the middle frame 

message_box = scrolledtext.ScrolledText(middle_frame,font=SMALL_FONT,bg=MEDIUM_GREY , fg =WHITE , width = 67 , height=27) #Creating a scrollable message box that will display all messages
message_box.config(state = tk.DISABLED)#Disabling clients from directly adding texts over here
message_box.pack(side=tk.TOP) #.pack() used to place this at the top of the middle frame with no padding 

#Setting up a function that will listen for messages from the server
def listen_for_message_from_server(client): #This function is called and threaded in the connect function in this code itself  resp for listening for messages from other clients 
    while 1: #So that it keeps on listening 
        message = client.recv(2048).decode('utf-8') #Getting the message and decoding it
        if message != ' ': #If the message was not empty 
            username,content = message.split('~', 1) #Splitting the message at the ~ part where the first part will have the username and second part will have the message 
            add_message(f"[{username}] ~ {content}") #Adding the message on the centre message  box 
        else: #If the message is empty 
            messagebox.showerror("Invalid message","Empty message recieved") #Create a new window that will show the error 

def main():  
    root.mainloop()  #starting the loop / start the update of window frame by frame cause tkinter YES
    #communicate_to_server(client) #
    
if __name__ == '__main__':# checks if the script is being run as the main program and not imported as a module
    main()#Calling the main function 

