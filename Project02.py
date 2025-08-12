# Example of reading and writing files in Python

# Writing to a text file
# with open("hello.txt", "w") as file:
#   file.write("Hello, world!\n")
#   file.write("This is my first file.\n")

# Reading from the text file
# with open("hello.txt", "r") as file:
#   content = file.read()
# print("File contents:")
# print(content)

# Working with CSV files
# import csv
#  Writing to the CSV file
# with open("grades.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name", "Grade"])  
#     writer.writerow(["Alice", 85])
#     writer.writerow(["Bob", 92])
#  Reading from the CSV file
# with open("grades.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# import csv

# with open("age.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name", "Age"])
#     writer.writerow(["Alice", 30])
#     writer.writerow(["Bob", 25])  
    
# with open("age.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

