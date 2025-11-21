user = input("Enter text to write to the file:")

with open("output.txt","w") as file:
    file.write(user)
    print("data successfully writen to output.txt\n")

append_data = input("Enter additional text to append:")

with open("output.txt","a") as file:
    file.write(f"\n{append_data}")
    print("Data successfully append.\n")

print("Final content of output.txt:")

with open("output.txt","r") as file:
    data = file.read()
    print(data)