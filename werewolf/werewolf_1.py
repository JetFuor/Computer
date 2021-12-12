# Using TCP Chatroom
# Be able to assign roles to each player
# 1 werewolf and everyone else is a villager
# Over time can add more roles that can be fun
# At first can type in chat with each other
# After specified time limit, all chat stops and werewolf can choose someone to kill
# When someone dies, no longer able to type in chat
# Next day they talk again, and after end of the day they can vote on someone to kill
# If it is a villager, game keeps going
# If it is a werewolf, game finishes and villagers are the winner
# If there is 1 werewolf and 1 villager, werewolf wins
# Overtime may be able to add more roles to it

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

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            indicator = message.decode('ascii')
            placement = indicator.find(':')
            if indicator[placement+2:] == "Start":
                werewolf()
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

# Receiving / Listening Function
def receive():
    while True:
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

# Intro to the game and ask number roles later
def intromessage():
    broadcast('Welcome to Werewolf!')
    broadcast('____________________')
    # I'll work on this later, just keep it here for now

# Randomizing roles for the players, preset numbers for now
def randomroles():
    users = nicknames

    roles = [['Werewolf', 1], ['Villager', 1], ['Seer', 0]]
    '''
    broadcast('How many werewolves do you want?')
    roles[0][1] = integers(client)

    broadcast('How many seers do you want?')
    roles[2][1] = integers(client)

    roles[1][1] = len(users) - roles[0][1] - roles[2][1]
    '''
    playerroles = []

    for i in range(len(users)):
        playerroles.append(["Name", "Roll"])

    for i in range(len(roles)):
        role = roles[i][0]
        numofplayers = roles[i][1]
        playersgiven = 0
        while playersgiven != numofplayers:
            userindex = random.randint(0, len(users)-1)
            if users[userindex] == '':
                continue
            else:
                playerroleindex = 0
                while playerroles[playerroleindex][0] != "Name":
                    playerroleindex += 1
                playerroles[playerroleindex][0] = users[userindex]
                playerroles[playerroleindex][1] = role
                users[userindex] = ''
                playersgiven += 1

    print(playerroles)

# Start off with first day, timer to type in chat
# Night phase starts, werewolf gets to choose to kill, temporary only do one
# Once chosen, person can no longer type in chat
# Next day they can type in chat and talk together
# At end of day phase, everyone vote to kill someone
# Person chosen can no longer type
# If werewolf chosen, villager win and game done
# Cycle repeats until 1 villager and 1 werewolf left, then werewolf wins
def game():
    pass

# Werewolf main
def werewolf():
    intromessage()
    randomroles()
    game()

print("Server is listening...")
receive()