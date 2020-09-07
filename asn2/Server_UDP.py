import socket
import datetime

# code written by William Ngo for CS3357

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
properQuestion = "What is the current date and time?"

while True:
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    mySocket.bind((UDP_IP, UDP_PORT))   #   still need to bind port when handling UDP server
    print("UDP server is now running...")   # no "handshake" or connection required, and we use datagrams which don't need a connection

    while True:
        data, clientAddress = mySocket.recvfrom(100)  #   since no connection to client established, we need to keep track of the client's address
        decodeData = data.decode()
        print("We received a request: ", decodeData)

        if decodeData.lower() == properQuestion.lower():
            rawDate = datetime.datetime.now()
            formattedDate = rawDate.strftime("%m/%d/%Y %H:%M:%S")
            dateMessage = "Current Date and Time: " + formattedDate
            mySocket.sendto(dateMessage.encode(), clientAddress)    #   send encoded message back to the address it came from
            break

        else:
            error = "Invalid question. Please enter your request again."
            mySocket.sendto(error.encode(), clientAddress)

    print()
    print("Waiting to receive another request...")











