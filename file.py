# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("This is line 1\n")
        file.write("2nd line with numbers: 42, 56.7\n")
        file.write("Line 3: Python is awesome!\n")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("File creation process completed.")

# File Reading and Display
try:

    with open("my_file.txt", "r") as file:
        print("Contents of my_file.txt:")
        for line in file:
            print(line.strip())
except Exception as e:
    print("An error occurred:", e)

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Additional line 1\n")
        file.write("Line 6: Appending more text\n")
        file.write("Last line appended\n")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("File appending process completed.")


