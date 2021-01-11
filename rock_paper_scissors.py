import random

def rockPaperScissors():
   player = input("Enter Rock, Paper, or Scissors: ")
   while(not(player == "Rock" or player == "Paper" or player == "Scissors")):
      player = input("Re-enter Rock, Paper, or Scissors: ")

   cpu = ""
   ran = random.randint(0, 2)
   if(ran == 0):
      cpu = "Rock"
   elif(ran == 1):
      cpu = "Paper"
   elif(ran == 2):
      cpu = "Scissors"

   if(player == cpu):
      print(f"Player: {player} vs CPU: {cpu} | Tie")
      rockPaperScissors()
   elif(player == "Rock" and cpu == "Paper"):
      print(f"Player: {player} vs CPU: {cpu} | CPU Wins")
   elif(player == "Scissors" and cpu == "Rock"):
      print(f"Player: {player} vs CPU: {cpu} | CPU Wins")
   elif(player == "Paper" and cpu == "Scissors"):
      print(f"Player: {player} vs CPU: {cpu} | CPU Wins")
   else:
      print(f"Player: {player} vs CPU: {cpu} | Player Wins")

rockPaperScissors()
