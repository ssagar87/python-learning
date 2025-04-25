#task 1
# try:
#     file1 = open("my_file.txt", "r")
#     output = file1.read()
#     print(output)
#     file1.close()
# except FileNotFoundError:
#     print("Error: The file 'my_file.txt' does not exist.")

#task 2
userInput = input("Enter text to write to the file: ")
file2 = open("my_file.txt", "w")
writing_file = file2.write(userInput)
file2.close()
if writing_file == 0:
    print("Failed to write to the file.")
else:
    print("Data successfully written to the my_file.txt.")

#task 3
userInput2 = input("Enter additional text to append: ")

file3 = open("my_file.txt", "a")
writing_file2 = file3.write("\n" +userInput2)
file3.close()
if writing_file2 == 0:
    print("Failed to append to the file.")
else:
    print("Data successfully appended to the my_file.txt.")

