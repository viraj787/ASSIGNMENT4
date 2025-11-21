import os
file_path = ".../sample.txt"
if os.path.exists(file_path):
    print("Error: The file 'sample.txt' was not found.")
else:
    print("Reading file content:")
    with open("sample.txt","r") as content:
        line1 = content.readline().rstrip("\n")
        line2 = content.readline()
        print(f"Line 1:{line1}")
        print(f"Line 2:{line2}")