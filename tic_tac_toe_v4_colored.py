# -*- coding: utf-8 -*-
"""tic tac toe V4 colored.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kbyd0KNLzOmvcV56qKkZcQon_YS2N-zN
"""

import os
class tictactoe:

  def __init__(s):
    print("Welcome to tic-tac-toe")
    print(f"0|1|2")
    print(f"-----")
    print(f"3|4|5")
    print(f"-----")
    print(f"6|7|8")
    s.total_turn=0
    s.__zero='0'
    s.__one='1'
    s.__two='2'
    s.__three='3'
    s.__four='4'
    s.__five='5'
    s.__six='6'
    s.__seven='7'
    s.__eight='8'
    s.turn='\033[32mX\033[0m'
    s.winnerfound=0
    s.isEnd=False
    s.is_Draw=False
  def printBoard(s):
    print(f"{s.__zero}|{s.__one}|{s.__two}")
    print(f"-----")
    print(f"{s.__three}|{s.__four}|{s.__five}")
    print(f"-----")
    print(f"{s.__six}|{s.__seven}|{s.__eight}")
  def Turn(s):
    iswrongmove=False
    if s.turn=='\033[32mX\033[0m':
      a=int(input('X\'s turn: '))
      if a==0 and s.__zero=='0':
        s.__zero='\033[32mX\033[0m'
      elif a==1 and  s.__one=='1':
        s.__one='\033[32mX\033[0m'
      elif a == 2 and s.__two=='2':
        s.__two ='\033[32mX\033[0m'
      elif a == 3 and s.__three=='3' :
        s.__three ='\033[32mX\033[0m'
      elif a == 4 and s.__four=='4':
        s.__four ='\033[32mX\033[0m'
      elif a == 5 and s.__five=='5':
        s.__five ='\033[32mX\033[0m'
      elif a == 6 and s.__six=='6':
        s.__six ='\033[32mX\033[0m'
      elif a == 7 and s.__seven=='7':
        s.__seven ='\033[32mX\033[0m'
      elif a == 8 and s.__eight=='8':
        s.__eight ='\033[32mX\033[0m'
      else:
        iswrongmove=True

      if iswrongmove==True:
        s.turn='\033[32mX\033[0m'
        print("Invalid move!")
      else:
        if s.total_turn<=9:
          s.turn='\033[31mO\033[0m'
          s.total_turn+=1

    else:
      a=int(input('Y\'s turn: '))
      iswrongmove=False
      if a==0 and s.__zero=='0':
        s.__zero='\033[31mO\033[0m'
      elif a==1 and  s.__one=='1':
        s.__one='\033[31mO\033[0m'
      elif a == 2 and s.__two=='2':
        s.__two ='\033[31mO\033[0m'
      elif a == 3 and s.__three=='3':
        s.__three ='\033[31mO\033[0m'
      elif a == 4 and s.__four=='4':
        s.__four ='\033[31mO\033[0m'
      elif a == 5 and s.__five=='5':
        s.__five ='\033[31mO\033[0m'
      elif a == 6 and s.__six=='6':
        s.__six ='\033[31mO\033[0m'
      elif a == 7 and s.__seven=='7':
        s.__seven ='\033[31mO\033[0m'
      elif a == 8 and s.__eight=='8':
        s.__eight ='\033[31mO\033[0m'
      else:
        iswrongmove=True

      if iswrongmove==True:
        s.turn="O"
        print("Invalid move!")
      else:
        if s.total_turn<=9:
          s.turn='\033[32mX\033[0m'
          s.total_turn+=1

  def WinCheck(s):
     if s.__zero==s.__one==s.__two=='\033[32mX\033[0m' or s.__three==s.__four==s.__five=='\033[32mX\033[0m' or s.__six==s.__seven==s.__eight=='\033[32mX\033[0m' or s.__zero==s.__three==s.__six=='\033[32mX\033[0m' or s.__one==s.__four==s.__seven=='\033[32mX\033[0m' or s.__two==s.__five==s.__eight=='\033[32mX\033[0m' or s.__zero==s.__four==s.__eight=='\033[32mX\033[0m' or s.__two==s.__four==s.__six=='\033[32mX\033[0m':
      print("Winner is X")
      s.isEnd=True
      return s.isEnd

     elif s.__zero==s.__one==s.__two=='\033[31mO\033[0m' or s.__three==s.__four==s.__five=='\033[31mO\033[0m' or s.__six==s.__seven==s.__eight=='\033[31mO\033[0m' or s.__zero==s.__three==s.__six=='\033[31mO\033[0m' or s.__one==s.__four==s.__seven=='\033[31mO\033[0m' or s.__two==s.__five==s.__eight=='\033[31mO\033[0m' or s.__zero==s.__four==s.__eight=='\033[31mO\033[0m' or s.__two==s.__four==s.__six=='\033[31mO\033[0m':
      s.winnerfound=1
      print("Winner is Y")
      s.isEnd=True
      return s.isEnd
    #  else:
    #   print("The match continues!")
  def isDraw(s):
    if s.total_turn==9:
      s.is_Draw=True
      return s.is_Draw
def tic_tac_toe():
  m=tictactoe()
  try:
    while True:

      flag=0
      m.Turn()
      os.system('cls')
      m.printBoard()
    # m.Turn()
      m.isDraw()
      m.WinCheck()

      if m.isEnd==True :
        print("End!")
        flag=1
      elif m.is_Draw==True:
        print("Draw!")
        flag=1
      if flag==1:
        v=input("Play again? y/n : ")
        if v=='y':
          tic_tac_toe()
        else:
          input("press enter to exit-")
          break



  except:
    print("invalid input!")
# input("Press enter to exit")
tic_tac_toe()