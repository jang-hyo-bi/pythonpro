print('YOur items:')
inventory = ('sword', 'armor', 'shield', 'healing potion')
for item in inventory:
	print(item)
print('\npress the enter key to continue.')
print('You have', len(inventory),'item in your possession')
print('\npress the enter key to continue.')
if 'healing potion' in inventory:
	print('You will live to fight another day.')
print('\nEnter the index number for an item in inventory:', end='')
tem=int(input(''))
print('At index',tem,'is',(inventory[tem]))
print('\nEnter the index number to begin a slice:', end='')
no1=int(input(''))
print('Ente the index number to end the slice:', end='')
no2=int(input(''))
print('inventory[', no1, ':', no2, ']           ', end='')
print(inventory[no1:no2])
print('\npress the enter key to continue.')
print('You find a chest. It cotains:')
chest = ('gold', 'gems')
print(chest)
print('You add the contents of the chest to your inventory.')
print('You inventory is now:')
inventory+=chest
print(inventory[:])
print ('\nPress the enter key to exit.') 
print ("You trade your sword for a crossbow.") 
inventory =["sword", "armor", "shield", "healing potion", "gold", "gems"] 
print ("Your inventory is now: ") 
inventory[0] = "crossbow" 
print (inventory) 
print ("\nPress the enter key to continue") 
print ("You use your gold and gems to buy an orb of future telling.") 
inventory =["crossbow", "armor", "shield", "healing potion", "gold", "gems"] 
print ("Your inventory is now: ") 
inventory[4:6] =["orb of future telling"] 
print (inventory) 
print ("\nPress the enter key to continue") 
print ("In a great battle, your shield is destroyed.") 
print ("Your inventory is now: ") 
inventory = ["crossbow", "armor", "shield", "healing potion", "orb of future telling"]
del inventory[2]
print(inventory)
print ("\nPress the enter key to continue") 
print ("Your crossbow and armor are stolen by thieves") 
inventory = ["crossbow", "armor", "healing potion","orb of future telling"]
del inventory[:2]
print("Your inventory is now: ")
print(inventory)
