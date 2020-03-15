from socket import *

localIP = "192.168.86.45"
serverPort = 20001
bufferSize = 1024

# Create a datagram socket
serverSocket = socket(AF_INET, SOCK_DGRAM) 

# Bind to address and ip
serverSocket.bind((localIP, serverPort)) 

print("The server is ready to receive") 

# Listen for incoming datagrams
while(True):
    encodedMessage, clientAddress = serverSocket.recvfrom(bufferSize) 
    message = encodedMessage.decode()
    serverMessage = ""

    clientMsg = "Message from Client: {}".format(message)
    clientIP  = "Client IP Address:{}".format(clientAddress)

    print(clientMsg)
    print(clientIP)

    if message == "Online":
      serverMessage = "Selected Online"

    elif message == "query for peers":
      serverMessage = "Selected query for peers"

    elif message == "Joined":
      serverMessage = "Selected Joined"
    
    elif message == "exit chatroom":
      serverMessage = "Selected exit chatroom"

    elif message == "Offline":
      serverMessage = "Selected Offline"
    
    else:
      serverMessage = "Invalid Command"
    
    # Sending a reply to client
    serverSocket.sendto(serverMessage.encode(), clientAddress)