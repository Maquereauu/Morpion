from math import *
import random

def Morpion():
  l = [0] * 9
  lenx = 3
  leny = 3
  dict_Morpion = {
    "haut-gauche": 0,
    "haut-milieu": 1,
    "haut-droite": 2,
    "milieu-gauche": 3,
    "milieu-milieu": 4,
    "milieu-droite": 5,
    "bas-gauche": 6,
    "bas-milieu": 7,
    "bas-droite": 8
  }
  grid_Morpion = [['□'] * lenx for i in range(leny)]
  while True:
    try:
      rules = int(input("Souhaitez vous connaître les règles?(0=>Non)"))
      break
    except ValueError:
      print("Veuillez mettre un entier,non pas un string >:(")

  if rules:
    print(dict_Morpion)
  symbolchoice = symbol()
  player1symbol = symbolchoice[0]
  player2symbol = symbolchoice[1]
  actual = player1symbol
  player1 = True

  while True:
    if player1:
      print("Au tour de P1:")
      player = str(input("Joueur 1 ,veuillez choisir "))
    if player1 == False:
      print("Au tour de P2:")
      player = str(input("Joueur 1 ,veuillez choisir "))
    if player in dict_Morpion and l[dict_Morpion[player]] == 0:
      player = dict_Morpion[player]
      l[player] = 1
      grid_Morpion[floor(player / lenx)][player % leny] = actual
    else:
      try:
        int(player)
      except ValueError:
        print("Ce n'est pas un coup possible >:(")
        continue
      player = int(player)
      if player > 8 or player < 0 or l[player] == 1:
        print("Ce n'est pas un coup possible >:(")
        continue
      for keys in dict_Morpion.keys():
        if player == dict_Morpion[keys]:
          l[player] = 1
          grid_Morpion[floor(player / lenx)][dict_Morpion[keys] % leny] = actual
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
            return "ligne diagonale,player1 gagne,GG"
          elif grid_Morpion[x][y] == player1symbol and grid_Morpion[x-1][y+1] == player1symbol and grid_Morpion[x+1][y-1] == player1symbol:
            return "ligne diagonale,player1 gagne,GG"
          elif grid_Morpion[x][y] == player2symbol and grid_Morpion[x-1][y-1] == player2symbol and grid_Morpion[x+1][y+1] == player2symbol:
            return "ligne diagonale,player2 gagne,GG"
          elif grid_Morpion[x][y] == player2symbol and grid_Morpion[x-1][y+1] == player2symbol and grid_Morpion[x+1][y-1] == player2symbol:
            return "ligne diagonale,player2 gagne,GG"
    if posY.count("0") == 3 or posY.count("1") == 3 or posY.count("2") == 3:
      if player1:
        return "ligne vertical,player1 gagne,GG"
      else:
        return "ligne vertical,player2 gagne,GG"
    if posX.count("0") == 3 or posX.count("1") == 3 or posX.count("2") == 3:
      if player1:
        return "ligne horizontale,player1 gagne,GG"
      else:
        return "ligne horizontale,player2 gagne,GG"
    if l.count(1) == 9:
      return "Draw -_-"
    if player1:
      player1 = False
      actual = player2symbol
      continue
    if player1 == False:
      player1 = True
      actual = player1symbol



def symbol():
  symbolchosen = str(input("Choisissez votre symbole(Croix ou Cercle)"))
  if symbolchosen == "Croix":
    symboll = ['X','♥','X','X','X','X','X','X']
    randomSymbol = random.choice(symboll)
    if randomSymbol == 'X':
      return ['X', 'O']
    elif randomSymbol == '♥':
      return ['X', '♥']
  elif symbolchosen == "Cercle":
    symboll = ['O','♥','O','O','O','O','O','O']
    randomSymbol = random.choice(symboll)
    if randomSymbol == 'O':
      return ['O', 'X']
    elif randomSymbol == '♥':
      return ['♥', 'X']
  else:
    return symbol()
