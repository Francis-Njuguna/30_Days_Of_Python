#file Handling in Python
#Creating and writing a file in python
with open("myfile.txt","a") as file:
  file.write("This is a new text /n")


with open("myfile.txt","r") as file:
  print(file.read())


#overwriting a file
with open("myfile.txt", "w") as file:
  file.write("This is overwritten text")
with open("myfile.txt","r") as file:
  print(file.read())

address= str(input("Enter your file name or address:"))

try:
  with open(address, "w") as file:
    file.write("File opened successfully but fuck")
except FileNotFoundError:
  print("File not found")   
# checking for a particular text in the file
with open(address, "r") as file:
  content = file.read()
  if "fuck" in content :
    print("Inappropriate Language found")
  else:
    print("Text has appropriate language")