# Your comment text here
# Deniz Keskin
import os

def calculate_table_to_file():
    # Check if text file exists, if yes then delete it
    # Create a file with the 'append' parameter.
    # Numbers 1-10 get multiplied by the index of the row they are in
    # Your code here
    if os.path.exists("calculation_table.txt"):
        os.remove("calculation_table.txt")
    file = open("calculation_table.txt", "a")
    currentRow = 1
    while currentRow <= 10:
        for i in range(1, 11):
            file.write(str(currentRow * i))
            file.write(' ')
        currentRow += 1
        file.write('\n')
    file.close()
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate_table_to_file()
