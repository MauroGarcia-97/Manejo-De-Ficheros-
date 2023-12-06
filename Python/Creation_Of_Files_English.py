import os

def Create_file():
    
    File_Name = input("Enter The Name Of The File You Want To Create: ")
    with open(File_Name, 'w') as File:
        print("The File Was Created Successfully.")

def Read_file():
    File_Name = input("Enter the Name of the File You Want to Read: ")
    with open(File_Name, 'r') as File:
        Content = File.read()
        print("The Content Of The File Is:")
        print(Content)

def Add_data():
    File_Name = input("Enter The Name Of The File You Want To Modify:")
    Element = input("Enter The Item You Want To Add:")
    with open(File_Name, 'a') as File:
        File.write(Element + "\n")
        print("The Item Was Added Successfully.")

def Modify_data():
    File_Name = input("Enter The Name Of The File You Want To Modify: ")
    with open(File_Name, 'r') as File:
        Lines = File.readlines()

    print("The Content Of The File Is:")
    for i, Line in enumerate(Lines):
        print(f"{i}: {Line}", end='')

    Number_Line = int(input("Enter The Line Number You Want To Modify:"))
    New_Line = input("Enter The New Line:")
    Lines[Number_Line] =  New_Line + "\n"

    with open(File_Name, 'w') as File:
        File.writelines(Lines)
        print("The Lines Were Successfully Modified.")

def Delete_data():
    File_Name = input("Enter The Name Of The File You Want To Delete: ")
    os.remove(File_Name)
    print("The File Was Successfully Deleted.")

while True:
    Menu = ('''  
            Menu
        1. Create A File.
        2. Read A File
        3. Add Elements To A File
        4. Modify A File
        5. Delete The File
        6. Exit
        Select An Option Between:''')
    
    option = input(Menu)

    match option: 
        case '1':
            Create_file ()
        case '2':
            Read_file()
        case '3':
            Add_data()
        case '4':
            Modify_data()
        case '5':
            Delete_data()
        case '6':
            print("Coming Out...")
            break
        case _:
            print("Invalid Option, Please Try Again.")
