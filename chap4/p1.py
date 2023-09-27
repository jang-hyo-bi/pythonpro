import random
mood=random.randrange(2)
print("I sense your energy. Your true emotions are coming across my screen.")
if mood == 0:
 print("you are....")
 print("__________")
 print(":        :")
 print(":o    o  :")
 print(":  <     :")
 print(":-    -  :")
 print(": '  '   :")
 print(":________:")
 print("...today")

elif mood == 1:
 print("you are....")
 print("__________")
 print(":        :")
 print(":o    o  :")
 print(":  <     :")
 print(": ---    :")
 print(":________:")
 print("...today")

elif mood == 2:
 print("you are....")
 print("__________")
 print(":         :")
 print(":y    y   :")
 print(":   <     :")
 print(": ~~~~    :")
 print(":_________:")

else: 
 print ("Illegal mood value!")
