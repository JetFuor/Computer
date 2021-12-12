import threading
import socket
import random

host = '127.0.0.1' #localhost
port = 55555 # don't choose betwen 0 and 10000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

checkstart = False

def broadcast(message):
    if checkstart:
        pass
    else:
        for client in clients:
            client.send(message)


def connectingplayers():
    while len(clients) != 2:
        # Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Request And Store Nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=messaging, args=(client,))
        thread.start()

    print("DID IT!")

def messaging(client):
    global message
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break

def inputsth():
    message = ""
    while message != "":
        message = client.recv(1024)

def startgame():
    broadcast('Type "Start" to start the game.'.encode('ascii'))
    checkstart = True
    while checkstart:
        indicator = message.decode('ascii')
        placement = indicator.find(':')
        if indicator[placement+2:] == "Start":
            break
    print("worked")

def intromessage():
    broadcast("Hello all players. Welcome to Werewolf!")

def main():
    print("Waiting...")
    connectingplayers()
    startgame()


main()