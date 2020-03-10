
""" Filesortingprogram """
from tkinter import *
from tkinter import filedialog
import sys
import os

import datetime

def formatTime(date_stat):
    return datetime.datetime.fromtimestamp(date_stat).strftime('%Y-%m')

import platform

def creationDate(path_to_file):  
    if platform.system() == 'Windows':
        return formatTime(os.path.getctime(path_to_file))
    else:
        stat = os.stat(path_to_file)
        try:
            return formatTime(stat.st_birthtime)
        except AttributeError:
            return formatTime(stat.st_mtime)

def browseButton():
    #Allow user to select a directory
    #filename is used as path in other functions
    #pathLabel is used as label for path in GUI
    global filename
    global pathLabel
    filename = filedialog.askdirectory()
    pathLabel.set(filename)
    
    print("Files in folder :")
    print(os.listdir(filename))
    print("Folderpath: \n" + filename)
    
    return filename
    


#button enabler to avoid error when pressing buttons in wrong order
def enableButtons():
    buttonSort.config(state=NORMAL)
    buttonSort2.config(state=NORMAL)
    buttonRemove.config(state=NORMAL)
    print("Enabled buttons.")

       
#function combiner to execute 2 functions when browse button is pressed
def combineFuncs(*funcs):
    def combinedFunc(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combinedFunc

import os
import shutil


def sortButton2():

    path = str(filename)
    os.chdir(path)
    
    filesInPath = os.listdir(path)
    
    filesToSort = []

    for files in filesToSort:
        if files.endswith(".txt"):
            filesToSort.append(files)

    print(filesToSort)

    foldersToMake = []

    for files in filesToSort:
        if not os.path.isdir(creationDate(path + '/' + files)):
            foldersToMake.append(creationDate(path + '/' + files))

    for folders in foldersToMake:
        os.mkdir(folders)
    print(foldersToMake)

    for files in filesToSort:
        shutil.move(path + '/' + files, path + '/' + creationDate(path + '/' + files))
        print(files + " moved")
        
    print("Files sorted.")
        
        
def sortButton():
    #Sort files in browsed directory according to filetype
    
    path = str(filename)
    os.chdir(path)
    
    filesToSort = os.listdir(path)
    print(filesToSort)

   


    
            
    

    """
    
    t = {i.lower() for i in filesToSort}

    for files in filesToSort:
        if files not in t:
            filesToSort.append(files)
    print(filesToSort)
    """
    
    folderName = ["text", "kalkyl", "DWG", "PDF", "GEO", "Backup"]
    fileType = [".odt", ".ods", ".dwg", ".pdf", ".geo", ".bkp"]
    #sets the lenght of loops
    fileTypeRange = len(fileType)

    subFolderName = ["PP", "Inmätningar"]
    
    subFileType = ["pp" , "inm"]
    #sets the lenght of loops
    subFileTypeRange = len(subFileType)
    

    #List with number of filetypes in boolean used for the sorting algo
    fileTypeChecked = []
    for item in fileType:
        fileTypeChecked.append(False)

    for item in subFileType:
        fileTypeChecked.append(False)
    print(fileTypeChecked)
    
    #Check to see if filesToSort exists in dir before making of folders
    for x in range(fileTypeRange):
        for file in filesToSort: 
            if file.endswith(fileType[x]):
                del fileTypeChecked[x]
                fileTypeChecked.insert(x, True)

    #Check to see if filesToSortLower exists in dir before making of folders
    for x in range(subFileTypeRange):
        for file in filesToSort:
            if file.startswith(subFileType[x]):
                del fileTypeChecked[fTL + x]
                fileTypeChecked.insert(fTL + x, True)
    
           
    print("Filetypes in directory")
    print(fileType + subFileType)
    print(fileTypeChecked)    
        
    #Make folders of folderName for fileTypes
    for x in range(fileTypeRange):
        if not os.path.exists(path + '/' + folderName[x]) and os.path.basename(path) != folderName[x] and fileTypeChecked[x] == True:
            os.makedirs(path + '/' + folderName[x])
            print("Created folder: " + path + '/' + folderName[x]) 
          
    #Make folders of subFolderName for subFileTypes
    for x in range(subFileTypeRange):
        if not os.path.exists(path + '/GEO/' + subFolderName[x]) and fileTypeChecked[fTL + x] == True:
            os.makedirs(path + '/GEO/' + subFolderName[x])
            print("Created subfolder: " + path + '/GEO/' + subFolderName[x])  

    for x in range(fileTypeRange):
        for files in filesToSort:
            if fileType[x] in files and not os.path.exists(path + '/' + folderName[x] + '/' + files):
                shutil.move(path + '/' + files, path + '/' + folderName[x] + '/')
                print("Moved file: " + path + '/' + files)
    
    for x in range(subFileTypeRange):
        for files in filesToSort:
            if subFileType[x] in files and not os.path.exists(path + '/GEO/' + subFolderName[x] + '/' + files):
                shutil.move(path + '/GEO/' + files, path + '/GEO/' + subFolderName[x] + '/')
                print("Moved file: " + path + '/' + files)
    
    sortingComplete = "Done"
    

def removeEmptyFolders():
    path = str(filename)
    os.chdir(path)
    filesToRemove = os.listdir(path)
    
    # remove empty subfolders
    if len(filesToRemove):
        for files in filesToRemove:
            filePath = os.path.join(path, files)              
            if os.path.isdir(filePath) and len(os.listdir(filePath)) == 0:
                os.rmdir(fullpath)
                
                print("Removed empty folder: " + filePath)
                removedLabel.set(filePath)

    # remmove empty folders
    if len(filesToRemove) == 0:
        print("Removed empty folder:", path)
        os.rmdir(path)
   
    print("Done.")



#GUI
root = Tk()
root.title("Filesorter beta 4.0")

labelHeader = Label(root, text="Filesorter")
labelHeader.config(font=("Courier", 25))
labelHeader.grid(row=0 ,column=1)

labelInstruction = Label(root, text="Browse folder to be sorted.")
labelInstruction.config(font=("Courier", 10))
labelInstruction.grid(row=1, column=1)

buttonBrowse = Button(text="Browse", command=combineFuncs(browseButton, enableButtons))
buttonBrowse.grid(row=3, column=2)
                      
pathLabel = StringVar()
labelPath = Label(master=root,textvariable=pathLabel)
labelPath.grid(row=3, column=1)

buttonSort = Button(text="Sort by file", command=sortButton, state=DISABLED)
buttonSort.grid(row=4, column=2)

buttonSort2 = Button(text="Sort by date", command=sortButton2, state=DISABLED)
buttonSort2.grid(row=5, column=2)

removedLabel = StringVar()
labelRemoved = Label(master=root,textvariable=removedLabel)
labelRemoved.grid(row=6, column=1)

buttonRemove = Button(text="Remove empty folders", command=removeEmptyFolders, state=DISABLED)
buttonRemove.grid(row=6, column=2)

mainloop()
