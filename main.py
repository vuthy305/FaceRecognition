#import relevant library
from tkinter import *
from tkinter import messagebox
from datetime import date
import time
import video
import folder,structuringdata,datapreprocessing,eigenimage,training

def trainImage():
    structuringdata.createDataFrameForTrain()
    datapreprocessing.dataPreProcessing()
    eigenimage.eigenImage()
    training.training()
def getAttendance():
    video.getAttendance()
def clearText(entryname):
    entryname.delete(0,END)
def takePhoto():
    if len(_userIDEntry.get()) == 0 and len(_userNameEntry.get()) == 0:
        messagebox.showerror("Error","No input in UserID and Username box was found!")
    elif len(_userIDEntry.get()) == 0:
        messagebox.showerror("Error","No input in UserID box was found!")
    elif len(_userNameEntry.get()) == 0:
        messagebox.showerror("Error","No input in UserName box was found!")
    else:
        response = folder.createNewFolder(_userIDEntry.get()+"-"+_userNameEntry.get())
        if (response == True):
            _notificationStatusLabel.config(text="Success")
            fol_name = _userIDEntry.get()+"-"+_userNameEntry.get()
            uname = _userNameEntry.get()
            result = video.takePhoto(fol_name, uname)
            if (result == True):
                messagebox.showinfo("Notification","50 Image Taken Successfully. Please Click On Train Image Button To Train Data.")
            else:
                messagebox.showerror("Error","Take Image Failed")

        else:
            _notificationStatusLabel.config(text="This user already exists.")

# function to open camera
def callOutVideo():
    video.openCamera()
# function to quit the application
def quitTheApplication():
    # Variable to receive the value from user click Yes or No
    response = messagebox.askyesno("Notification","Do you want to exit the application?")
    # Check if response == 1 mean user click on Yes
    if response == 1:
        # function to close the window 
        window.quit()
# function to get current date
def getDate():
    # variable to receive the current date
    getDate = date.today()
    # convert the date to format with - and store in variable today
    Today = getDate.strftime("%b-%d-%Y")
    # after getting the value we return it
    return Today
# function to get current time
def getTime():
    # variable to receive the current date and make its in the format
    Time = time.strftime("%I:%M:%S %p")  
    # return the time with the format
    return Time
# function to combine the date and time together and auto reload to view date and time on screen
def getDateTime():
    # variable to receive the current date
    getDate = date.today()
    # convert the date to format with - and store in variable today
    Today = getDate.strftime("%b-%d-%Y")
    # variable dateTime to store string of Date and Time
    dateTime = Today + "|" + time.strftime("%I:%M:%S %p")  
    # add the value of date and time to dateTime Label
    dateTimeLabel.config(text = dateTime)
    # auto reload the function to get time update
    dateTimeLabel.after(200,getDateTime)
# main function 
def main():
    # Initiate the window application
    global window
    window = Tk()
    # Get the width and heigh of the computer or laptop screen which application is running on
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # Set the title and size of application by set full screen and widown resizable
    window.title("Face Attendance System")
    window.geometry(f"{width}x{height}")
    window.resizable(0,0)
    # Title Label
    _titleLabel = Label(window,text="FACE ATTENDANCE SYSTEM",font=("Calibri",20,"bold"),background="#949494",foreground="#ffffff")
    _titleLabel.pack(fill=X,ipady=height*0.08)
    # Right Side Frame
    _rightSide = Frame(window,background="#BEBEBE",width=int(width*0.5))
    _rightSide.pack(side=RIGHT,fill=Y)
    # Left Side Frame
    _leftSide = Frame(window,width=int(width*0.5))
    _leftSide.pack(side=LEFT,fill=Y)
    # Update the window to get the new value of all widget that we have inputted
    window.update()
    # Get the Left Side Frame width and height
    _lWidth = _leftSide.winfo_width()
    _lHeight = _leftSide.winfo_width()
    # Take Attendance title which place in the Left Side Frame
    _takeAttendanceLabel = Label(_leftSide,text="TAKE ATTENDENCE",width=_lWidth,font=("Calibri",20,"bold"),pady=20,fg="#333333")
    _takeAttendanceLabel.config(anchor="center")
    _takeAttendanceLabel.pack()
    # Declare the dateTimeLabel to show the date and time of Left Side Frame
    global dateTimeLabel 
    dateTimeLabel =  Label(_leftSide,width=_lWidth,font=("Calibri",15,"bold"),fg="#3E3D53",)
    dateTimeLabel.config(anchor="center")
    dateTimeLabel.pack()
    # Frame place on Left Side Frame to show the user detail after getting their faces 
    showNameFrame = Frame(_leftSide,width=int(_lWidth*0.9),background="#ffffff",height=int(_lHeight*0.4))
    showNameFrame.pack(pady=20)
    # Button to get the attendance location in Left Side Frame
    takeAttendanceButton = Button(_leftSide,text="TAKE ATTENDANCE",width=int(_lWidth*0.04),height=int(_lHeight*0.004),font=("Calibri",10,"bold"),command=getAttendance)
    takeAttendanceButton.pack()
    # Button to quit the application location in Left Side Frame
    quitButton = Button(_leftSide,text="QUIT",width=int(_lWidth*0.04),height=int(_lHeight*0.004),font=("Calibri",10,"bold"),background="#ec7a7a",activebackground="#f2a5a5",command=quitTheApplication)
    quitButton.pack()
    # Get the Right Side Frame width and height
    _rWidth = _rightSide.winfo_width()
    _rHeight = _rightSide.winfo_width()
    # New Registration title which place in the Left Side Frame
    _newRegistrationLabel = Label(_rightSide,text="NEW REGISTRATION",width=50,font=("Calibri",20,"bold"),pady=20,fg="#333333")
    _newRegistrationLabel.config(anchor="center")
    _newRegistrationLabel.pack()
    # User ID Label
    _userIDLabel = Label(_rightSide,font=("Calibri",0,"bold"),text="USER ID",fg="#333333")
    _userIDLabel.config(anchor="center",width=50,font=("Calibri",10,"bold"))
    _userIDLabel.place(rely=0.18,height=30)
    # User ID Entry
    global _userIDEntry
    _userIDEntry = Entry(_rightSide,width=50,font=("Calibri",10,"bold"),)
    _userIDEntry.place(rely=0.18,relx=0.30,height=30)
    # User ID Clear Button
    _clearUserIDButton = Button(_rightSide,text="CLEAR",foreground="#333333",font=("Calibri",10,"bold"),background="#ec7a7a",activebackground="#f2a5a5",command=lambda: clearText(_userIDEntry)).place(rely=0.18,relx=0.85,height=30,width=70)
    # User Name Label
    _userNameLabel = Label(_rightSide,font=("Calibri",0,"bold"),text="USERNAME",fg="#333333")
    _userNameLabel.config(anchor="center",width=50,font=("Calibri",10,"bold"))
    _userNameLabel.place(rely=0.25,height=30)
    # User Name Entry
    global _userNameEntry
    _userNameEntry = Entry(_rightSide,width=50,font=("Calibri",10,"bold"))
    _userNameEntry.place(rely=0.25,relx=0.30,height=30)
    # User Name Clear Button
    _clearUserNameButton = Button(_rightSide,text="CLEAR",foreground="#333333",font=("Calibri",10,"bold"),background="#ec7a7a",activebackground="#f2a5a5",command=lambda: clearText(_userNameEntry)).place(rely=0.25,relx=0.85,height=30,width=70)
    # Notification Entry
    _notificationLabel = Label(_rightSide,font=("Calibri",0,"bold"),text="NOTIFICATION",fg="#333333")
    _notificationLabel.config(anchor="center",font=("Calibri",10,"bold"))
    _notificationLabel.place(rely=0.35,height=30,relwidth=0.5)
    # Notification Status
    global _notificationStatusLabel
    _notificationStatusLabel = Label(_rightSide,font=("Calibri",0,"bold"),text="",fg="#333333",background="#fff")
    _notificationStatusLabel.config(anchor="center",font=("Calibri",10,"bold"))
    _notificationStatusLabel.place(rely=0.35,relx=0.5,height=30,relwidth=0.5)
    # Detection Button
    _detectionButton = Button(_rightSide,text="DETECTION",foreground="#ffffff",font=("Calibri",10,"bold"),background="#3e3d53",activebackground="#696880",activeforeground="#fff",command=callOutVideo).place(rely=0.45,relx=0.03,height=40,relwidth=0.3)
    # Take Phto Button
    _takePhotoButton = Button(_rightSide,text="TAKE PHOTO",foreground="#ffffff",font=("Calibri",10,"bold"),background="#7f7d9c",activebackground="#adadc9",activeforeground="#fff",command=takePhoto).place(rely=0.45,relx=0.35,height=40,relwidth=0.3)
    # Train Button
    _trainButton = Button(_rightSide,text="TRAIN IMAGE",foreground="#ffffff",font=("Calibri",10,"bold"),background="#32eac5",activebackground="#5fefd2",activeforeground="#fff",command=trainImage).place(rely=0.45,relx=0.67,height=40,relwidth=0.3)
    # Check Attendance Label
    _checkAttendanceLabel = Label(_rightSide,text="CHECKING ATTENDANCE",width=50,font=("Calibri",20,"bold"),pady=20,fg="#333333").place(rely=0.55,relx=0.0,height=60,relwidth=1.0)
    # Check Attendance Button
    _checkAttendanceButton = Button(_rightSide,text="CHECK ATTENDANCE",foreground="#ffffff",font=("Calibri",10,"bold"),background="#59515e",activebackground="#4d4c5c",activeforeground="#fff",command=callOutVideo).place(rely=0.70,relx=0.0325,height=60,relwidth=0.935)
    # Callback function to reload time
    getDateTime()
    # Function to make loop the application 
    window.mainloop()
# Call main function to run the application
if __name__ == "__main__":
    main()