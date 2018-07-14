
players = ['lihong', 'qiuping', 'pingping', 'shufeng', 'meinv']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

copy_players = players[:]
print(copy_players)

for player in players[:3]:
    print(player)