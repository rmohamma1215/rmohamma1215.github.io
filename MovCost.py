#Company Header below
print('''
==============================================================================
            ______         __  ___                   ______                
           / ____/___     /  |/  /___ _   _____     / ____/___  _________  
          / / __/ __ \   / /|_/ / __ \ | / / _ \   / /   / __ \/ ___/ __ \ 
         / /_/ / /_/ /  / /  / / /_/ / |/ /  __/  / /___/ /_/ / /  / /_/ / 
         \____/\____/  /_/  /_/\____/|___/\___/   \____/\____/_/  / .___(_)
                                                               /_/       
==================== EASY AND ENJOYABLE MOVE WITH US =========================
''')

#INTRO
print('''
Thank you for contacting us. 
We will help your moving process. Please fill below required information: 
''')

#QUEST1 below
print('''
1. What is your apartment size, select between option 1 to 4.
   1. 1R
   2. 1DK
   3. 1LDK
   4. 2LDK
''')

answer1 = input("Define your answer here: ")
answer1f = "Your room type: {}".format(answer1)
answer1 = int(answer1)

if(answer1 == 1):
   print(answer1f)
elif(answer1 == 2):
   print(answer1f)
elif(answer1 == 3):
   print(answer1f)
elif(answer1 == 4):
   print(answer1f)
else:
   print("Please only select the option 1 to 4")

#QUEST2 below
print('''
------------------------------------------------------------------------------
2. How long is the distance from the origin to the destination in KM? 
   Please refer to google maps (https://www.google.co.jp/maps)
''')

answer2 = input ("Define your answer here (Km): ")
answer2f = "The apartment distance: {} Km.".format(answer2)
answer2 = int(answer2)
D1 = int(answer2)
print(answer2f)

#QUEST3 below
print('''
------------------------------------------------------------------------------
3. How many items with all dimensions less than 1m?
''')

answer3 = input("Define your answer here: ")
answer3f = "Total item: {}, which less than 1m".format(answer3)
answer3 = int(answer3)
T3 = int(answer3)
print(answer3f)

#QUEST4 below
print('''
------------------------------------------------------------------------------
3. How many items with all dimensions more than 1m?
''')

answer4 = input("Define your answer here: ")
answer4f = "Total item: {}, which more than 1m".format(answer4)
answer4 = int(answer4)
T4 = int(answer4)
print(answer4f)

#CONFIRM below
print('''
------------------------------------------------------------------------------
Please make sure below conditions is correct, before we start the calculation.
''')
print(answer1f)
print(answer2f)
print(answer3f)
print(answer4f)
print('''
Is everything is fine?
''')
answer4 = input ("Define your answer here (y/n): ")
answer4f = str(answer4)

import time
if(answer4 == "y"):
   print("Thank you for your confirmation. We are proceessing the cost calculation.")
   time.sleep(10)
elif(answer4 == "n"):
   print("Please refresh you page to redo the process")
else:
   print("Please only select 'y' or 'n'")

#COSTCALCPROCESS below
if(D1> 20):
   disccost = 10000
else:
   disccost = 5000

totdim = T3 + T4
if(totdim > 20):
   dimcost = 30000
else:
   dimcost = 15000

totcost = disccost + dimcost

if(totdim > 10):
   trucksize = "Large"
else:
   trucksize = "Small"

totcosttx = "Your Total Cost: JPY {}".format(totcost)
print(totcosttx)
trucksizetx = "Truck Size: {}".format(trucksize)
print(trucksizetx)

#CLOSING below
print('''
for reservations reach us on customer service call at +81 707-7890-1234
''')

