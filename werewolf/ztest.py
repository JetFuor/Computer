import random

users = ['Jeff', 'Kurt', 'Henry', 'Rick']

roles = [['Werewolf', 0], ['Villager', 0], ['Seer', 0]]

roles[0][1] = int(input("How many werewolves do you want: "))
roles[2][1] = int(input("How many seers do you want: "))

roles[1][1] = len(users) - roles[0][1] - roles[2][1]

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