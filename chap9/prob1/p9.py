class Critter:
	"A virtual pet"
	def talk(self):
		print("Hi. I'm an instance of class Critter.")
#main
crit  = Critter()
crit.talk()

print("Press the enter key to exit.")
while True:
	n = input("")
	if n =="":
		break;
