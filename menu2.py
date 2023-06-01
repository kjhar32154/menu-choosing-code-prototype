from time import sleep
import csv
import os

writeFile = "d"
fileExtName = ".mnu"
addItemToFile = ""

def optionrrr(writeFile):
    writeFile = []
    askOption=int(input("Please type which function to use: \n1.See the menu \n2.Add an item \n3.Delete an item \n4.Look up menu \n5.Go back\n"))

    if askOption == 1:
        if writeFile == []:
            print("Please enter another option because there isn't an object in menu ")
            sleep(1)
            optionrrr()
        else:
            for x in writeFile:
                print(x)
            sleep(5)    
    elif askOption == 2: 
        addObject = input("Type the new object to the menu: ")
        line = int(input("Which number do you want to insert it to?  "))
        writeFile.insert(line,addObject)
    elif askOption == 3:
        if writeFile ==[]:
            print("Please enter another option because there isn't an object in menu ")
            sleep(1)
            optionrrr()
        else: 
            deleteObject = input("Type the object to delete from the menu ")
            writeFile.remove(deleteObject)
    elif askOption == 4 :
        asklen = input("Type up the item you are searching for: ")
        if asklen in writeFile == True:
            print("There is " + asklen + "in your menu.")
            sleep(3)
            optionrrr()
    elif askOption == 5:
        main()
    else:
        return 
    
def createFile():
    writeFile = input("Please create a name for the menu ")
    with open(writeFile + fileExtName, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(writeFile)
        
def showFileInDir():
    hasFile = 0 
    for x in os.listdir():
        if x.endswith(fileExtName):
            hasFile = 1
            # Prints only text file present in My Folder
            print(x)
    if (hasFile != 1):
        print("[No menu yet]")
            
def main():       
    print("List menu files")
    showFileInDir()
    askFile = int(input("Please type function you want to use: \n1. Make a file \n2. Delete file \n3. Open file\n>"))
    
    if askFile == 1:
        createFile()
    elif askFile == 2:
        print("Type the file name to delete")
        showFileInDir()
        deleteFile = input("")
        print("Deleting " + deleteFile)
        if os.path.exists(deleteFile):
            os.remove(deleteFile)
            print("you successfully deleted an item")
        else:
            print("You don't have any things to delete.")
            sleep(4)
            main()
    elif askFile == 3:
        print("Type the file name to add the item(s)")
        showFileInDir()
        addItemToFile = input("")                        
        optionrrr(addItemToFile)
   

while True:
    main()
