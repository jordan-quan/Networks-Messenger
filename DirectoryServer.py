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
    message, clientAddress = serverSocket.recvfrom(bufferSize) 
    modifiedMessage = message.decode().upper() 
  
    clientMsg = "Message from Client:{}".format(modifiedMessage)
    clientIP  = "Client IP Address:{}".format(clientAddress)
    
    print(clientMsg)
    print(clientIP)

    # Sending a reply to client
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)