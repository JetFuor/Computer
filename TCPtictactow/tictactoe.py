
import threading
import socket
import random
import os
import time

# Clears up the terminal
os.system('cls')

host = '127.0.0.1' #localhost
port = 55555 # don't choose betwen 0 and 10000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Stores where to send and names
clients = []
nicknames = []

board = """
   A     B     C  
1     |     |     
 -----+-----+-----
2     |     |     
 -----+-----+-----
3     |     |     
"""

# Moves player can chooose
placements = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

# Sending messages to all the players
def broadcast(message):
    for client in clients:
        client.send(message)

# Handles any messages coming in
def handle(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024) # Waits to receive a message
            broadcast(message)
            testplacement(message)
            replay(message)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break

# Receiving / Listening Function
def getplayers():
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
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

# Deciding who goes first
def playerorder():
    global index
    global p1
    global p2
    index = random.randint(0,1)
    p1 = clients[index]
    p1.send("You are X and going first.".encode('ascii'))
    # Messages are sent to the opposite player
    if index == 0:
        p2 = clients[1]
        p2.send("You are O and going second.".encode('ascii'))
    else:
        p2 = clients[0]
        p2.send("You are O and going second.".encode('ascii'))

# Starting off the game
def firstround():
    p1.send(board.encode('ascii'))
    moves = str(placements)
    p1.send("Choose your move out of the following - ".encode('ascii'))
    p1.send(moves.encode('ascii'))

# Seeing if the message sent is a move on the board
def testplacement(message):
    test = message.decode('ascii')
    index = test.find(':')
    test = test[index+2:]
    if test in placements:
        boardchange(test)

turn = 0
p1moves = []
p2moves = []

# Changing the board since a choice has been made
def boardchange(location):
    global finished
    global placements
    global turn
    global board
    if not finished:
        turn += 1
        # Checking whose turn it is
        if turn % 2 == 1: # p1 turn
            letter = "X"
            p1moves.append(location)
        else: # p2 turn
            letter = "O"
            p2moves.append(location)
        # Changing the board to include X or O
        if location == "A1":
            board = board[:23] + letter + board[24:]
        elif location == "A2":
            board = board[:29] + letter + board[30:]
        elif location == "A3":
            board = board[:35] + letter + board[36:]
        elif location == "B1":
            board = board[:61] + letter + board[62:]
        elif location == "B2":
            board = board[:67] + letter + board[68:]
        elif location == "B3":  
            board = board[:73] + letter + board[74:]
        elif location == "C1":
            board = board[:99] + letter + board[100:]
        elif location == "C2":
            board = board[:105] + letter + board[106:]
        elif location == "C3":
            board = board[:111] + letter + board[112:]
        # Removes it from the list so it can't be selected again
        placements.remove(location)
        # Once it is possible, it checks when there are winners
        if turn > 4:
            checkwin()
        # Checking by the time all moves have been done, if no winner it is a tie and ends game
        if not finished:
            if turn == 9:
                finished = True
                broadcast("Tie. No winner.".encode('ascii'))
                time.sleep(0.5)
                broadcast("Type REPLAY to play again.".encode('ascii'))
        # Sending the moves to the next players to take their turn
        if not finished:
            broadcast(board.encode('ascii'))
            moves = str(placements)
            if turn % 2 == 1:
                p1.send("It is the other players turn now.".encode('ascii'))
                p2.send("Choose your move out of the following - ".encode('ascii'))
                p2.send(moves.encode('ascii'))
            else:
                p2.send("It is the other players turn now.".encode('ascii'))
                p1.send("Choose your move out of the following - ".encode('ascii'))
                p1.send(moves.encode('ascii'))

finished = False

# Checking if someone won the game
def checkwin():
    global finished
    # Seeing which list of moves they want to see
    if turn % 2 == 1:
        checkmoves = p1moves
    else:
        checkmoves = p2moves
    # Checking every possible winning combination
    if "A1" in checkmoves and "A2" in checkmoves and "A3" in checkmoves:
        finished = True
    elif "B1" in checkmoves and "B2" in checkmoves and "B3" in checkmoves:
        finished = True
    elif "C1" in checkmoves and "C2" in checkmoves and "C3" in checkmoves:
        finished = True
    elif "A1" in checkmoves and "B1" in checkmoves and "C1" in checkmoves:
        finished = True
    elif "A2" in checkmoves and "B2" in checkmoves and "C2" in checkmoves:
        finished = True
    elif "A3" in checkmoves and "B3" in checkmoves and "C3" in checkmoves:
        finished = True
    elif "A1" in checkmoves and "B2" in checkmoves and "C3" in checkmoves:
        finished = True
    elif "A3" in checkmoves and "B2" in checkmoves and "C1" in checkmoves:
        finished = True
    # Saying which player wins
    if finished:
        if turn % 2 == 1: # Shows player 1 wins
            broadcast((nicknames[index] + " has won!").encode('ascii'))
            time.sleep(0.5)
            broadcast("Type REPLAY to play again.".encode('ascii'))
        elif index == 1: # Shows player 2 wins
            broadcast((nicknames[0] + " has won!").encode('ascii'))
            time.sleep(0.5)
            broadcast("Type REPLAY to play again.".encode('ascii'))
        else: # Shows player 2 wins
            broadcast((nicknames[1] + " has won!").encode('ascii'))
            time.sleep(0.5)
            broadcast("Type REPLAY to play again.".encode('ascii'))

# Setting up the start
def game():
    broadcast("START".encode('ascii'))
    time.sleep(1)
    playerorder()
    firstround()

# Ability to reset the game and play again
def replay(indicator):
    global board
    global turn
    global p1moves
    global p2moves
    global placements
    global finished
    # Checking if the game is over yet
    if finished:
        word = indicator.decode('ascii')
        colon = word.find(':')
        # Only if they say REPLAY can the game reset
        if word[colon+2:] == 'REPLAY':
            # Resetting all the default values back again
            finished = False
            board = """
   A     B     C  
1     |     |     
 -----+-----+-----
2     |     |     
 -----+-----+-----
3     |     |     
"""
            turn = 0
            p1moves = []
            p2moves = []
            placements = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"] 
            game()

print("Server is listening...")
getplayers()
game()
