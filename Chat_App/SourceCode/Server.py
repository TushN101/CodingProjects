#importing all the modules 
import socket #importing the socket module necessary for networking tasks 
import threading #importing the threading module helps to run multiple multiple threads

HOST = '127.0.0.1' #Setting the host the server will be hosten on
PORT = 1234 #Setting the port anything other than the general ports that are being used on which the server will be ported on
LISTENER_LIMIT = 5 #Setting the max limit of clients that would be there
active_clients=[] #Setting the list of all active clients

#Setting the function to better format the message and then pass on the function that will send the message
def listen_for_message(client , username): #Taking in the parameters of the client object and the username 
    while 1: #Setting it as while loop so it keeps listening for message     
        message = client.recv(2048).decode('utf-8') #Storing the message in the message variable after decoding it          
        if message != ' ': #If the message is not empty   
            final_msg =username+' ~ '+ message  #Formatting the message so that it has username and message               
            send_messages_to_all(final_msg) #Sending the formatted message  to the function resp for sending message to all            
        else:#If the message is empty 
            print(f"An empty message was sent from {username}") #Thowing a message if the message was empty 
            
#Setting the function to broadcast the message to client
def send_messages_to_all(final_msg):
    for user in active_clients: #As in for loop to send the message to all the users in the list of active users 
        send_messsage_to_client(user[1],final_msg) #So for each user call the funtion and pass it the user[1] which has client obj and message
        
#Setting the function to send the message to the single clients 
def send_messsage_to_client(client,message):
    client.sendall(message.encode()) #Sending that client with the client obj we got and sending it the message with encoding 

#Setting the function to handle the initialization of a new client connection in a chat server
def client_handler(client): #We are passing it the client object we recieved
    #Server listening to client message that will contain its username
    while 1: #So that this is always listening 
        username = client.recv(2048).decode('utf-8') #Taking the input of username max size 2048 and decoding that message 
        if username != ' ': #If the input username was not empty 
            active_clients.append((username,client)) #Then appending the username and the client object into the list of active clients
            prompt = "SERVER~" + f"{username} was added to the chat" #Making a prompt that the username client was added to the server
            send_messages_to_all(prompt) #Broadcasting the prompt that the client joined the server
            break #breaking the while loop
        else: #If the username was empty 
            print("Client has no username") #Throwing error of no username and since while 1: running username listener again

    threading.Thread(target=listen_for_message,args=(client,username, )).start() #After username accept , multi-threading the listen for message resp for listening message for that client clients object and its username
    
#Setting the main function that will run first 
def main():
    #Setting a new socket called server that uses IPv4(AF_INET) for addressing and supports reliable, stream-oriented communication using the TCP protocol(SOCK_STREAM)
    server  = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    try: #Tryinig to bind the server to the host ip and port 
        server.bind((HOST,PORT)) #Bind functon to bind the servers socket to the host and port 
        print(f"Server is running on {HOST} {PORT}") #Printing if the server socket was connnected succesfully 
    except: #A necessary except case as for the try is there 
        print(f"Unable to bind to host {HOST} and port {PORT}") #Showing the error that server couldnt bind to the host and port         
    server.listen(LISTENER_LIMIT) #Setting server limit
    
    while 1:
        #Always listen and accept a new connection from client / Returns a new socket (client) for communication with the client and the client's address (address).
        client , address = server.accept()
        #The address is a tuple
        #address[0]: The IP address of the client.
        #address[1]: The port number used by the client for the connection.
        print(f"Succesfully connect to client {address[0]} {address[1]}") #Printing the succesfully connection from the client with its IP and its PORT 
        threading.Thread(target=client_handler,args=(client, )).start() #Starting a multi threading of a function client handler allowing the server to handle multiple clients concurrently.
        
if __name__ == '__main__': # checks if the script is being run as the main program and not imported as a module
    main() #Calling the main function 