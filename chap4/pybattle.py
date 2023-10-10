import random

herohp = random.randrange(50, 101)
monsthp = random.randrange(50, 101)

print("hero HP: ", herohp, ", monster HP: ", monsthp)

i = 0
while herohp > 0 and monsthp > 0:
	
	heroat = random.randrange(-10, 21)
	monstat = random.randrange(-10, 21)

	if heroat > 0:
		result = "success"
		monsthp -= heroat
	else:
		result = "fail"

	if monstat > 0:
		result1 = "success"
		herohp -= monstat
	else:
		result1 = "fail"
	
	print("hero(HP:", herohp, ", attck:", heroat, result, "<-> monster(HP:", monsthp, ", attck:", monstat, ")", result1)
	i += 1

print("-----------------------------------------------")
print("Total phase: ", i, ",")
if herohp <= 0:
	print("Monster Win!!!!")
if monsthp <= 0:
	print("Hero Win!!!!")
