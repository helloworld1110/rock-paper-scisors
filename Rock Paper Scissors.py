#if you like, pls star

import random
import time

sleep = time.sleep

print("You have 5 lifes, watch out!")
sleep(1)

vidas = 5

pontos = 0

while vidas >= 1:
  
  if vidas == 0:
    print("Game Over...")
    sleep(1)
    print("Score:{}".format(pontos))
    break
  
  print(" ")
  print("[1] Rock")
  sleep(0.5)
  print("[2] Paper")
  sleep(0.5)
  print("[3] Scissor")
  sleep(0.5)
  print(" ")
  jogada = int(input("choose one: "))
  print(" ")
  sleep(1)
  
  ai = random.randint(1, 3)
  
  if jogada == 1 and ai == 1:
    print("Player: Rock")
    sleep(1)
    print("AI: Rock")
    sleep(1.5)
    print(" ")
    print("Draw!!")
    print(" ")
    print("======================")
    sleep(1)
  
  elif jogada == 1 and ai == 2:
    print("Player: Rock")
    sleep(1)
    print("AI: Paper")
    sleep(1.5)
    print(" ")
    print("Player lose...")
    sleep(0.5)
    vidas = vidas - 1
    print("You have {} lifes".format(vidas))
    print(" ")
    print("======================")
    sleep(1)
      
  elif jogada == 1 and ai == 3:
    print("Player: Rock")
    sleep(1)
    print("AI: Scissor")
    print(" ")
    sleep(1.5)
    print("Player wins!!!")
    sleep(0.5)
    pontos = pontos + 1
    print("You have {} points".format(pontos))
    print(" ")
    print("======================")
    sleep(1)
   
    
  if jogada == 2 and ai == 1:
    print("Player: Paper")
    sleep(1)
    print("AI: Rock")
    print(" ")
    sleep(1.5)
    print("Player wins!!!")
    sleep(0.5)
    pontos = pontos + 1
    print("You have {} points".format(pontos))
    print(" ")
    print("======================")
    sleep(1)
      
  elif jogada == 2 and ai == 2:
    print("Player: Paper")
    sleep(1)
    print("AI: Paper")
    print(" ")
    sleep(1.5)
    print("Draw!!")
    print(" ")
    print("======================")
    sleep(1)
    
  elif jogada == 2 and ai == 3:
    print("Player: Paper")
    sleep(1)
    print("AI: Scissor")
    print(" ")
    sleep(1.5)
    print("Player lose...")
    vidas = vidas - 1
    print("You have {} lifes".format(vidas))
    print(" ")
    print("======================")
    sleep(1)
    
  elif jogada == 3 and ai == 1:
    print("Player: Scissor")
    sleep(1)
    print("AI: Rock")
    print(" ")
    sleep(1.5)
    print("Player lose...")
    vidas = vidas - 1
    print("You have {} lifes".format(vidas))
    print(" ")
    print("======================")
    sleep(1)
    
  elif jogada == 3 and ai == 2:
    print("Player: Scissor")
    sleep(1)
    print("AI: Paper")
    print(" ")
    sleep(1.5)
    print("Player wins!!!")
    pontos = pontos + 1
    print("You have {} points".format(pontos))
    print(" ")
    print("======================")
    sleep(1)
    
  elif jogada == 3 and ai == 3:
    print("Player: Scissor")
    sleep(1)
    print("AI: Scissor")
    print(" ")
    sleep(1.5)
    print("Draw!!!")
    print(" ")
    print("======================")
    sleep(1)
  
  else:
    print("Invalid Choice!")
    print(" ")
    print("======================")
    sleep(1)