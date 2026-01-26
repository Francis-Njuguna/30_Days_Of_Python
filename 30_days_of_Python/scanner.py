#A little project I did o n day 5
address =  str(input("Enter your file name or location address:"))

try:
  with open(address, "r") as file:
    content = file.read().lower()
    if "debug = true" in content:
      print("Vulnarability Found ☠")
    else:
      print("You are safe for Prod😊")
except FileNotFoundError:
  print("file not found!!")
except Exception as e:
  print("An error occurred:", e)