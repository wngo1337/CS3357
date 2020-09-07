import socket
import datetime

# code written by William Ngo for CS3357

TCP_IP = "127.0.0.1"    #   apparently this is "standard loopback interface address?
TCP_PORT = 5005         #   not sure if the assignment meant we were allowed to choose the port, or if we were supposed to be able to listen on any port...


while True: #   When we close connection to the current client, we come back up here to wait for a new connection
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket.bind((TCP_IP, TCP_PORT))   #   configures our socket to interact with the given address and port
    mySocket.listen(1)
    properQuestion = "What is the current date and time?"

    connection, address = mySocket.accept() #   *new* socket and address of the incoming connection

    print("Our server address is: ", TCP_IP)
    print("New connection to address ", address, " established. Waiting for a request...")

    while True:
        data = connection.recv(100)  #   receive at most 100 bytes. Not sure how long this needs to be...
        decodeData = data.decode()
        print("The request we received is: ", decodeData)

        if decodeData.lower() == properQuestion.lower():    #   ignore capitalization on the request
            rawDate = datetime.datetime.now()
            formattedDate = rawDate.strftime("%m/%d/%Y %H:%M:%S")
            dateMessage = "Current Date and Time: " + formattedDate
            connection.sendall(dateMessage.encode())   #   sending the formatted string back to the client
            break   #   get out of message loop and wait for a new connection

        else:
            error = "Invalid question. Please enter your request again."
            connection.sendall(error.encode())

    print()
    mySocket.close()
    print("Connection to current client closed. Waiting on a new connection...")
