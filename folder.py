import os

parentDir = "Facedatabase/"

def getAllParentDirectory(parent):
    return os.listdir(parent)
def convertListElementToLowercase(list):
    nList = [element.lower() for element in list]
    return nList

def checkExistFolder(fol_name):
    # Get the list of all folder with its label
    path = getAllParentDirectory(parentDir)
    # Get the list of path in lower case
    # lPath = convertListElementToLowercase(path)
    # Check if the name was exist
    if fol_name in path:
        return False
    else:
        return True
def createNewFolder(dir_name):
    if checkExistFolder(dir_name):
        # Combine the path between parent and the directory name given
        path = os.path.join(parentDir,dir_name)
        # Make Directory with all the path 
        os.mkdir(path)
        return True
    else:
        return False