#Variables- this are conatiners for storing data values
x = 10
print(x)

firstName ="Francis"

#Global Variables
eg = "This is a global variable"

def myFunc():#this is a function in python the myFunc is the name of the function and we call it by myFunct()
  print(eg)
#calling the function
myFunc()

num1 =3
num2 =10

def sum(num1,num2):
  total= num1 +num2
  print("The sum is "+ str(total))
sum(num1,num2)

#data collection data types
#List- is a collection which is ordered and changeable. Allows duplicate members.
list1 = ["Apples", "Bananas", "Cherries"]
list2 = [1,2,3,4,5]

print(list1)
print(list2)

print(type(list1))
print(list1[1])
#to change an item in the list

list1[1] = "Mangoes"
print(list1)

#conditional statements
grade = 67

if(grade>=70):
    print("A")
elif(grade>=60):
    print("B")  
else:
    print("C")
    
#BMI Detector
height = float(input("Enter your height in meters:"))
weight = float(input("Enter your weight in kg:  "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 24.9:  
    print("Normal weight")
elif 25 <= bmi < 29.9:
    print("Overweight")
    
#loops
#counting from 1 to 5
for i in range(1,6):
    print(i)

#while loop
count =1

while count <=5:
    print(count)
    count +=1
#function to test if a number is even or odd  it should repeat itself implementing loops
print("----------------------------")
while True:   
  num  = int(input("Enter a number:   "))
  def evenOdd(num):
    if num % 2 ==0:
        print(str(num) + " is an Even number")
    else:
        print(str(num) + " is an Odd number") 
  evenOdd(num)
  repeat = input("Do you want to check another number? (yes/no): ").lower()
  if repeat != 'yes':
      break
