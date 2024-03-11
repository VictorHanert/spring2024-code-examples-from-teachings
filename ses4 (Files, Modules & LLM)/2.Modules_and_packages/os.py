import os

# Step 1: Create a folder named 'os_exercises'
folder_name = 'os_exercises'
os.makedirs(folder_name, exist_ok=True)

# Step 2: Create a file named 'exercise.py' inside the folder
file_name_1 = os.path.join(folder_name, 'exercise.py')
file_name_2 = os.path.join(folder_name, 'exercise2.py')

# Step 3: Get input from the console and write it to the file
input_content_1 = input("Enter content for exercise.py: ")
with open(file_name_1, 'w') as file:
    file.write(input_content_1)

input_content_2 = input("Enter content for exercise2.py: ")
with open(file_name_2, 'w') as file:
    file.write(input_content_2)

# Step 5: Read the content of the files and print it to the console
with open(file_name_1, 'r') as file:
    content_1 = file.read()
    print(f"Content of {file_name_1}:")
    print(content_1)

with open(file_name_2, 'r') as file:
    content_2 = file.read()
    print(f"\nContent of {file_name_2}:")
    print(content_2)
