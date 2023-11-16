print("Reating a text file with the write<> method.\n")

print("Reading the newly created file.")
text_file = open("write_it.txt", "w")

text_file.write("Line 1\n")
text_file.write("This is line 2\n")
text_file.write("That makes this line 3\n")
text_file.close()
text_file = open("write_it.txt", "r")

a_write = text_file.read()
print(a_write)
print("")

print("Creating a text file with the writelines<> method.\n")
print("Reading the newly created file.")

text_file = open("write_lines.txt", "w")
lines = ["Line 1\n", "This is line 2\n", "That makes this line 3\n"]

text_file.writelines(lines)
text_file.close()

text_file = open("write_lines.txt", "r")

b_write = text_file.read()
print(b_write)
print("\n")

text_file.close()
