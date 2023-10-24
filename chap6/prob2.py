print("\tHigh Scores Keeper")

scores = []
while True:
    
    print("")
    print("\t0 - Quit")
    print("\t1 - List")
    print("\t2 - Add a Score")
    print("")
    
    num_input = int(input("Choice: "))

    if num_input == 0:
        break

    if num_input == 2:
        name_input = input("What is the player's name?: ")
        score_input = int(input("What score did the player get?:"))
        scores.append((score_input, name_input))
    
    if num_input == 1:
        print("High Scores")
        print("")
        print("NAME\tSCORE")
        
        scores.sort()
        scores.reverse()
        
        for entry in scores:
            score_input, name_input = entry
            print(name_input, "\t", score_input)

