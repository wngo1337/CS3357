import socket

# code written by William Ngo for CS3357

TCP_IP = "127.0.0.1"
TCP_PORT = 5005

print("Give me a second, we're trying to connect to address ",TCP_IP," on port ", TCP_PORT)
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect((TCP_IP, TCP_PORT))
print("Connection to server established.")

while True: #   I think we are supposed to automatically close connection on valid input and response from server
    command = input("Please enter a command: ")
    mySocket.sendall(command.encode())
    data = mySocket.recv(100)   #   receive up to 100 bytes (chars). Probably don't need more than that right now...
    decodeData = data.decode()
    print("The server responded: ", decodeData)

    if "invalid" not in decodeData.lower(): #   condition for an invalid message is that it contains word "invalid"; otherwise the input is valid and we are done
        break

print()
print("Closing the connection...")
mySocket.close()
print("Connection to server closed. Goodbye.")
