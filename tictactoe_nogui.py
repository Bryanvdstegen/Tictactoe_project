import sys
game=[[2,2,2],[2,2,2],[2,2,2]]

def printboard(tgame):
  board = "\n"
  for row in tgame:
    if row[0] == 2:
      board+='|?|'
    elif row[0] == 0:
      board+='|X|'
    elif row[0] == 1:
      board+='|O|'
    if row[1] == 2:
      board+='?|'
    elif row[1] == 0:
      board+='X|'
    elif row[1] == 1:
      board+='O|'
    if row[2] == 2:
      board+='?|'
    elif row[2] == 0:
      board+='X|'
    elif row[2] == 1:
      board+='O|'
    board+='\n'
    print(board)
    print "\n\n"