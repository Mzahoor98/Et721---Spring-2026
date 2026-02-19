"""
Muhammad Zahoor
Feb 19, 2026
Lab 7, working with data in python
"""
print("\n ----- Example 1: read file")
with open("phrases.txt", "r") as file1:
    filecontent = file1.read(30)
    filecontent = file1.read(5)
    print(filecontent)

# Check if the file is closed.
print(f"Is the file closed?{file1.closed}")


print("\n ----- Example 2: readline file")
with open("phrases.txt", "r") as file1:
    filecontent = file1.read(30)
    print(filecontent)
    filecontent = file1.read(5)
    print(filecontent)

print("\n ----- Example 3: readlines file")
# readlines makes a list of all the lines in the text file. Each line is an item in the list.
with open("phrases.txt", "r") as file1:
    filecontent = file1.read()
    print(filecontent)
    filecontent = file1.read(5)
    print(filecontent)

print("\n ----- Example 4: loop through each line in a file")
with open("phrases.txt", "r") as file1:
    filecontent = file1.readlines()
    for eachline in filecontent:
        print(eachline.strip()) #strip() method removes \n in each line

print("\n ----- example 5: create file")
# w mode create a file if the file doesnt exist. On the other hand, if the file exists, w mode will overwrite the data
with open("zahoor.txt", "w") as file:  
    file.write("Python basics for data science\n")
    file.write("Muhammad Zahoor")

print("\n ----- Example 6: append data into an exsiting file")
# append the date and time into "zahoor.txt" file
from datetime import datetime

with open("zahoor.txt", "a") as file:
    file.write(f"\nLast update: {datetime.now()}")

print("\n----- Example 7: copy a file")
# copy file "zahoor.txt" into a new file
with open("zahoor.txt", "r") as readfile:
    with open("newfile.txt", "w") as writefile:
        for eachline in readfile:
            writefile.write(eachline)

print("\n----- Example 8: creating dataframe with pandas")
import pandas as pd

data ={
    'Name' : ['Alice','Bob','Charlie'],
    'Age' : [25,30,35]
}

df = pd.DataFrame(data)
print(df)

print("\n----- Example 9: creating df with pandas from an excel file")
df = pd.read_csv("data.csv")
print(df)
print(df.head())

print("\n----- Exercise: ")
def email_read():
    gmail_count = 0
    yahoo_count = 0
    hotmail_count = 0

    try:
        with open("user_email.txt", "r") as file:
            for line in file:
                email = line.strip().lower()

                if "@gmail.com" in email:
                    gmail_count += 1
                elif "@yahoo.com" in email:
                    yahoo_count += 1
                elif "@hotmail.com" in email:
                    hotmail_count += 1

        with open("reportemail.txt", "w") as report:
            report.write(f"gmail = {gmail_count}\n")
            report.write(f"yahoo = {yahoo_count}\n")
            report.write(f"hotmail = {hotmail_count}\n")

        print("gmail =", gmail_count)
        print("yahoo =", yahoo_count)
        print("hotmail =", hotmail_count)

    except FileNotFoundError:
        print("Error: user_email.txt file not found.")
    except Exception as e:
        print("An error occurred:", e)


email_read()

