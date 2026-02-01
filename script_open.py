with open("hello", "w") as file: #rewrite file
    file.write("Hello World\n")

with open("hello", "a") as file: # adding text in the same file
    file.write("Hello World\n")

with open("hello2", "x") as file: # create file only if the file_name doesn't exist
    file.write("Hello World\n")
