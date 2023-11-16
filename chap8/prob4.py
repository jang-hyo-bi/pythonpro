import pickle
print("Pickling litsts.\n")

print("Unpickling lists.")

variety = ["sweet", "hot", "dill"]
shape = ["whole", "spear", "chip"]
brand = ["Claussen", "Heinz", "Vlassic"]
pickle_file = open("pickles1.dat", "wb")
pickle.dump(variety, pickle_file)
pickle.dump(shape, pickle_file)
pickle.dump(brand, pickle_file)
pickle_file.close()


pickle_file = open("pickles1.dat", "rb") 
variety = pickle.load(pickle_file)
shape = pickle.load(pickle_file)
brand = pickle.load(pickle_file)
pickle_file.close()  
print(variety)
print(shape)
print(brand)

print("\nShelving lists.\n")
print("Retrieving the lists from a shelved file:")
import shelve
pickles = shelve.open("pickles2.dat")
pickles["variety"] = ["sweet", "hot", "dill"]
pickles["shpae"] = ["whole", "spear", "chip"]
pickles["brand"] = ["Claussen", "Heinz", "Vlassic"]
pickles.sync()

for key in pickles.keys():
    print(key, "-", pickles[key])


