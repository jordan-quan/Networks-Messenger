from socket import * 
serverName = "192.168.86.45"
serverPort = 20001
bufferSize = 1024

clientSocket = socket(AF_INET, SOCK_DGRAM)
message = raw_input("Input lowercase sentence: ") 
clientSocket.sendto(message.encode(),(serverName, serverPort)) 
modifiedMessage, serverAddress = clientSocket.recvfrom(bufferSize) 

print(modifiedMessage.decode())
clientSocket.close()