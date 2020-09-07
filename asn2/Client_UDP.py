import socket

# code written by William Ngo for CS3357

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #   no need for client to bind to a port when using UDP
print("Ready to contact server...")

while True:
    command = input("Please enter a command: ")
    mySocket.sendto(command.encode(), (UDP_IP, UDP_PORT))
    data, serverAddress = mySocket.recvfrom(100)
    decodeData = data.decode()

    print("The server responded: ", decodeData)

    if "invalid" not in decodeData.lower():
        break

print()
print("Request successful. Goodbye.")
