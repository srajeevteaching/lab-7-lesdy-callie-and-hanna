import random
#Programmers: Callie Walker, Lesdy Galvez, Hanna Magan
#Date: 11/4/21
#Lab Number: 7
#Program Inputs: number from dice roll,
#Program Outputs: Number of asteriks for each number

i = 0
userInput = int(input("Enter amount of rolls "))
dice = [2,3,4,5,6,7,8,9,10,11,12]
new = [0,0,0,0,0,0,0,0,0,0,0]
#Roll the dice to see what numbers are rolled and how many times
#if i = index - 1 i+=1
count = 2
for i in range(2,12):
    print(i)
for i in range(userInput):
    roll = random.randint(2, 12)
    new[roll-2] += 1
    print(roll, "*", end="")
    print()
print(new)