from math import *
from random import *

def Morpion(isFirst=1):
  l = [0] * 9
  lenx = 3
  leny = 3
  dict_Morpion = {
    "haut-gauche": 7,
    "haut-milieu": 8,
    "haut-droite": 9,
    "milieu-gauche": 4,
    "milieu-milieu": 5,
    "milieu-droite": 6,
    "bas-gauche": 1,
    "bas-milieu": 2,
    "bas-droite": 3
  }
  index_values = {
    7: 0,
    8: 1,
    9: 2,
    4: 3,
    5: 4,
    6: 5,
    1: 6,
    2: 7,
    3: 8
  }
  grid_Morpion = [['□'] * lenx for i in range(leny)]
  if isFirst:
    while True:
      try:
        rules = int(input("Souhaitez vous connaître les règles?(0=>Non)"))
        break
      except ValueError:
        print("Veuillez mettre un entier,non pas un string >:(")
    if rules:
      print(dict_Morpion)
  while True:
      multiplayer = input("Voulez-vous jouer contre un humain ou bien contre un robot?")
      multiplayer = multiplayer.upper()
      if multiplayer in ["ROBOT",'R']:
        robot = True
        break
      if multiplayer in ["HUMAIN",'H']:
        robot = False
        break
      else:
        print("Veuillez écrire soit robot,soit humain(ou bien r ou h)")
  symbolchoice = symbol()
  player1symbol = symbolchoice[0]
  player2symbol = symbolchoice[1]
  whoplays = randint(0,1)
  if whoplays == 0:
    player1 = True
    actual = player1symbol
    print("Joueur 1 joue en premier")
  if whoplays == 1:
    player1 = False
    actual = player2symbol
    print("Joueur 2 joue en premier")

  while True:
    if robot:
      if player1:
        print("Au tour de P1:")
        player = str(input("Joueur 1 ,veuillez choisir "))
        if player == "ratio":
          print("Player 1 a gagné? ah oui...🤓")
          return playAgain()
        if player in dict_Morpion and l[index_values[dict_Morpion[player]]] == 0:
          player = index_values[dict_Morpion[player]]
          l[player] = 1
          grid_Morpion[floor(player / lenx)][player % leny] = actual
        else:
          try:
            int(player)
          except ValueError:
            print("Ce n'est pas un coup possible >:(")
            continue
          player = int(player)
          if not(player in index_values):
            print("Ce n'est pas un coup possible >:(")
            continue
          player = index_values[player]
          if player > 8 or player < 0 or l[player] == 1:
            print("Ce n'est pas un coup possible >:(")
            continue
      if player1 == False:
        print("Au tour de l'IA:")
        player = IA(grid_Morpion,player1symbol,player2symbol)
        for keys in index_values:
          if player == index_values[keys]:
            for key in dict_Morpion:
              if dict_Morpion[key] == keys:
                print("L'ia va jouer à la case "+key)
    if robot == False:
      if player1:
        print("Au tour de P1:")
        player = str(input("Joueur 1 ,veuillez choisir "))
        if player == "ratio":
          print("Player 1 a gagné? ah oui...🤓")
          return playAgain()
      if player1 == False:
        print("Au tour de P2:")
        player = str(input("Joueur 2 ,veuillez choisir "))
        if player == "ratio":
          print("Player 2 a gagné? ah oui...🤓")
          return playAgain()
      if player in dict_Morpion and l[index_values[dict_Morpion[player]]] == 0:
          player = index_values[dict_Morpion[player]]
          l[player] = 1
          grid_Morpion[floor(player / lenx)][player % leny] = actual
      else:
        try:
          int(player)
        except ValueError:
          print("Ce n'est pas un coup possible >:(")
          continue
        player = int(player)
        if not(player in index_values):
          print("Ce n'est pas un coup possible >:(")
          continue
        player = index_values[player]
        if player > 8 or player < 0 or l[player] == 1:
          print("Ce n'est pas un coup possible >:(")
          continue
    for keys in index_values.keys():
      if player == index_values[keys]:
        l[player] = 1
        grid_Morpion[floor(player / lenx)][index_values[keys] % leny] = actual
    for k in range(lenx):
      print("\n",'' + '   |   '.join(grid_Morpion[k]) + '',"\n")
    posX = []
    posY = []
    for x in range(lenx):
      for y in range(leny):
        if grid_Morpion[x][y] == player1symbol and player1 == True or grid_Morpion[x][y] == player2symbol and player1 == False:
          posX.append(str(x))
          posY.append(str(y))
        if x == 1 and y == 1:
          if grid_Morpion[x][y] == player1symbol and grid_Morpion[x-1][y-1] == player1symbol and grid_Morpion[x+1][y+1] == player1symbol:
            print("ligne diagonale,player1 gagne,GG")
            return playAgain()
          elif grid_Morpion[x][y] == player1symbol and grid_Morpion[x-1][y+1] == player1symbol and grid_Morpion[x+1][y-1] == player1symbol:
            print("ligne diagonale,player1 gagne,GG")
            return playAgain()
          elif grid_Morpion[x][y] == player2symbol and grid_Morpion[x-1][y-1] == player2symbol and grid_Morpion[x+1][y+1] == player2symbol:
            print("ligne diagonale,player1 gagne,GG")
            return playAgain()
          elif grid_Morpion[x][y] == player2symbol and grid_Morpion[x-1][y+1] == player2symbol and grid_Morpion[x+1][y-1] == player2symbol:
            print("ligne diagonale,player1 gagne,GG")
            return playAgain()
    if posY.count("0") == 3 or posY.count("1") == 3 or posY.count("2") == 3:
      if player1:
        print("ligne verticale,player1 gagne,GG")
        return playAgain()
      else:
        print("ligne verticale,player1 gagne,GG")
        return playAgain()
    if posX.count("0") == 3 or posX.count("1") == 3 or posX.count("2") == 3:
      if player1:
        print("ligne horizontale,player1 gagne,GG")
        return playAgain()
      else:
        print("ligne horizontale,player2 gagne,GG")
        return playAgain()
    if l.count(1) == 9:
      print("Draw -_-")
      return playAgain()
    if player1:
      player1 = False
      actual = player2symbol
      continue
    if player1 == False:
      player1 = True
      actual = player1symbol


def symbol():
  symbolchosen = str(input("Choisissez votre symbole(Croix ou Cercle)"))
  randomvalue=randint(0,10)
  if symbolchosen in ["Croix","croix",'X','x']:
    if randomvalue == 5:
      return ['🤠','🐄']
    return ['X', 'O']
  if symbolchosen in ["Cercle","cercle","O","o"]:
    if randomvalue == 5:
      return ['🤠', '🐄']
    return ['O', 'X']
  else:
    return symbol()


def playAgain():
  playInput = input("Voulez-vous rejouer ?")
  if playInput in ["Oui","OUI","oui",'y',"yes","Yes","YES"]:
    return Morpion(0)
  return "Oh :("


def IA(board,symbolPlayer,symbolAI):
  c=0
  X = []
  Y = [[""]*3 for i in range(3)]
  Diag1 = []
  Diag2 = []
  for x in range(3):
    X.append(board[x])
    for y in range(3):
      Y[x][y]=board[y][x]
  for k in range(3):
    for i in range(3):
      if k == 0 and i==0 or k==1 and i==1 or k==2 and i==2:
        Diag1.append(X[k][i])
      if k == 0 and i==2 or k==1 and i==1 or k==2 and i==0:
        Diag2.append(X[k][i])
  corners =[Diag1[0],Diag1[2],Diag2[0],Diag2[2]]
  corners_id=[0,8,2,6]
  for j in range(3):
    for l in range(3):
      if board[j][l] == '□':
        c += 1
  if c == 9:
    return 0
  for i in range(3):
    if X[i].count(symbolAI) == 2 and X[i].count(symbolPlayer) !=1:
      for j in range(3):
        if X[i][j] != symbolAI:
          return j+(i*3)
    if Y[i].count(symbolAI) == 2 and Y[i].count(symbolPlayer) !=1:
      for j in range(3):
        if Y[i][j] != symbolAI:
          return i+(j*3)
    if Diag1.count(symbolAI) == 2 and Diag1[i].count(symbolPlayer) !=1:
      if Diag1[i] != symbolAI:
        return i*4
    if Diag2.count(symbolAI) == 2 and Diag2[i].count(symbolPlayer) !=1:
      if Diag2[i] != symbolAI:
        return 2+(i*2)
  for l in range(3):
    if X[l].count(symbolPlayer) == 2 and X[l].count(symbolAI) !=1:
      for j in range(3):
        if X[l][j] != symbolPlayer:
          return j+(l*3)
    if Y[l].count(symbolPlayer) == 2 and Y[l].count(symbolAI) !=1:
      for j in range(3):
        if Y[l][j] != symbolPlayer:
          return l+(j*3)
    if Diag1.count(symbolPlayer) == 2 and Diag1[l].count(symbolAI) !=1:
      if Diag1[l] != symbolPlayer:
        return l*4
    if Diag2.count(symbolPlayer) == 2 and Diag2[l].count(symbolAI) !=1:
      if Diag2[l] != symbolPlayer:
        return 2+(l*2)
  if corners.count('□') == len(corners):
    return 0
  for i in range(3):
    for j in range(3):
      if i == 1 and (j == 0 or j == 2):
        if j == 2:
          if board[i][j] == symbolPlayer and board[i][0] == '□':
            return i+j
        if j == 0:
          if board[i][j] == symbolPlayer and board[i][2] == '□':
            return board[i][2]
      if j == 1 and (i == 0 or i == 2):
        if board[i][j] == symbolPlayer:
          if i == 0 and board[2][j] == '□':
            return (2*3)+j
          if board[i][j] == '□':
            return j
  if corners.count(symbolAI) == 0 and corners.count(symbolPlayer) == 1:
    if board[1][1] == '□':
      return 4
  for i in range(0,3,2):
    for j in range(0,3,2):
      if Y[i].count(symbolPlayer) == 1 and Y[i].count('□') == 2 and X[j].count(symbolPlayer) == 1 and X[j].count('□') == 2:
        if X[j][1] == '□':
          return (j*3)+1
  for i in range(0,3,2):
    if Diag1.count(symbolPlayer) == 1 and Y[i].count(symbolPlayer) == 1 and Diag1[0] == '□':
      if board[1][1] == '□':
        return 4
      for j in range(3):
        if Y[i][j] == '□':
          return (3*j)+i
    if Diag2.count(symbolPlayer) == 1 and Y[i].count(symbolPlayer) == 1 and Diag2[0] == '□':
      if board[1][1] == '□':
        return 4
      for j in range(3):
        if Y[i][j] == '□':
          return (3*j)+i
  if corners.count(symbolAI) == 1 and corners.count(symbolPlayer) == 0:
    for i in range(len(corners)):
      if corners[i] == symbolAI:
        if i == 1 or i == 3:
          return corners_id[i-1]
        return corners_id[i+1]
  else:
    for i in range(3):
      for j in range(3):
        if board[i][j] == '□':
          return i*3+j


print(Morpion())
