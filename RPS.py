import os

ch = 'y'
while ch == 'y':
  a = input("Enter the A choice:")
  os.system('cls')
  b = input("Enter the B choice:")
  os.system('cls')
  if a == "Rock" and b == "Paper":
    print("B wins!\n")
  elif a == "Rock" and b == "Scissors":
    print("A wins!\n")
  elif a == "Paper" and b == "Scissors":
    print("B wins!\n")
  elif a == "Paper" and b == "Rock":
    print("A wins!\n")
  elif a == "Scissors" and b == "Rock":
    print("B wins!\n")
  elif a == "Scissors" and b == "Paper":
    print("A wins!\n")
  elif a == b:
    print("Oh! It's a draw\n")
  else:
    print("Please use only (Rock/Paper/Scissors)\n")
  ch = input("Want to continue playing?(y/n)")
  print("\n")