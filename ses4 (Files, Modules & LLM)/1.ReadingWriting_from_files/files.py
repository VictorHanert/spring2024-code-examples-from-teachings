# Create a file called numbers.dat and write numbers from 1 to 100
with open("numbers.dat", "w") as file:
    for i in range(1, 101):
        file.write(str(i) + "\n")

# Open the file for reading and print all even numbers to the screen
with open("numbers.dat", "r") as file:
    for line in file:
        number = int(line.strip())
        if number % 2 == 0:
            print(number)