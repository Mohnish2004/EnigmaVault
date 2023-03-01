import hashlib
import sqlite3
from functools import partial
from tkinter import *
from tkinter import simpledialog
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from passgen import passGenerator


# Database_connection

with sqlite3.connect("Enigma_vault.db") as db:
    cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS masterpassword(
id INTEGER PRIMARY KEY,
password TEXT NOT NULL);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS vault(
id INTEGER PRIMARY KEY,
platform TEXT NOT NULL,
account TEXT NOT NULL,
password TEXT NOT NULL);
""")

# Creating different PopUps

def copyPass1(password):
    window.clipboard_clear()
    window.clipboard_append(password)

def popUp(text):
    answer = simpledialog.askstring("input string", text)
    return answer

def popUp_blank(text):
    answer = messagebox.showinfo("Info", text)
    return answer

def popUp_button(text, password):
    answer1 = messagebox.showinfo("Info", text)
    answer2 = messagebox.askquestion("Copy Password?", "Do you want to copy the password?", icon="question")
    if answer2 == "yes":
        copyPass1(password)
        m="Password copied sucessfully"
        answer3 = messagebox.showinfo("Nice",m)
  
        
# Initiating Window

window = Tk()
window.update() 

window.title("ENIGMA VAULT")



# Encryptions for master password
def UTF_encrypt(input):
    hash1 = hashlib.md5(input)
    hash1 = hash1.hexdigest()
    return hash1

def Caesar_encrypt(input,shift=11):
    encrypted=""
    for i in range (len(input)):
        char = input[i]
        if (char.isupper()):
            encrypted += chr((ord(char)+shift -65)% 26 + 65)
        elif (char.islower()):
            encrypted += chr((ord(char)+shift - 97) % 26 + 97)
        elif (char.isdigit()):
            number = (int(char)+shift) % 10
            encrypted += str(number)
        else:
            encrypted += char
    return encrypted

rotors = ("I","II","III")
reflector = "UKW-B"
ringSettings ="ABC"
ringPositions = "DEF"
plugboard = "AT BS DE FM IR KN LZ OW PV XY"

def caesarShift(str, amount):
	output = ""

	for i in range(0,len(str)):
		c = str[i]
		code = ord(c)
		if ((code >= 65) and (code <= 90)):
			c = chr(((code - 65 + amount) % 26) + 65)
		output = output + c

	return output

def Enigma_encrypt(plaintext):
  global rotors, reflector,ringSettings,ringPositions,plugboard
  #Enigma Rotors and reflectors
  rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
  rotor1Notch = "Q"
  rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
  rotor2Notch = "E"
  rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
  rotor3Notch = "V"


  rotorDict = {"I":rotor1,"II":rotor2,"III":rotor3}
  rotorNotchDict = {"I":rotor1Notch,"II":rotor2Notch,"III":rotor3Notch}

  reflectorB = {"A":"Y","Y":"A","B":"R","R":"B","C":"U","U":"C","D":"H","H":"D","E":"Q","Q":"E","F":"S","S":"F","G":"L","L":"G","I":"P","P":"I","J":"X","X":"J","K":"N","N":"K","M":"O","O":"M","T":"Z","Z":"T","V":"W","W":"V"}
  reflectorC = {"A":"F","F":"A","B":"V","V":"B","C":"P","P":"C","D":"J","J":"D","E":"I","I":"E","G":"O","O":"G","H":"Y","Y":"H","K":"R","R":"K","L":"Z","Z":"L","M":"X","X":"M","N":"W","W":"N","Q":"T","T":"Q","S":"U","U":"S"}

  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  rotorANotch = False
  rotorBNotch = False
  rotorCNotch = False

  if reflector=="UKW-B":
    reflectorDict = reflectorB
  else:
    reflectorDict = reflectorC

  #A = Left,  B = Mid,  C=Right
  rotorA = rotorDict[rotors[0]]
  rotorB = rotorDict[rotors[1]]
  rotorC = rotorDict[rotors[2]]
  rotorANotch = rotorNotchDict[rotors[0]]
  rotorBNotch = rotorNotchDict[rotors[1]]
  rotorCNotch = rotorNotchDict[rotors[2]]

  rotorALetter = ringPositions[0]
  rotorBLetter = ringPositions[1]
  rotorCLetter = ringPositions[2]

  rotorASetting = ringSettings[0]
  offsetASetting = alphabet.index(rotorASetting)
  rotorBSetting = ringSettings[1]
  offsetBSetting = alphabet.index(rotorBSetting)
  rotorCSetting = ringSettings[2]
  offsetCSetting = alphabet.index(rotorCSetting)

  rotorA = caesarShift(rotorA,offsetASetting)
  rotorB = caesarShift(rotorB,offsetBSetting)
  rotorC = caesarShift(rotorC,offsetCSetting)

  if offsetASetting>0:
    rotorA = rotorA[26-offsetASetting:] + rotorA[0:26-offsetASetting]
  if offsetBSetting>0:
    rotorB = rotorB[26-offsetBSetting:] + rotorB[0:26-offsetBSetting]
  if offsetCSetting>0:
    rotorC = rotorC[26-offsetCSetting:] + rotorC[0:26-offsetCSetting]

  ciphertext = ""

  #Converplugboard settings into a dictionary
  plugboardConnections = plugboard.upper().split(" ")
  plugboardDict = {}
  for pair in plugboardConnections:
    if len(pair)==2:
      plugboardDict[pair[0]] = pair[1]
      plugboardDict[pair[1]] = pair[0]

  plaintext = plaintext.upper()
  for letter in plaintext:
    encryptedLetter = letter

    if letter in alphabet:
      #Rotate Rotors - This happens as soon as a key is pressed, before encrypting the letter!
      rotorTrigger = False
      #Third rotor rotates by 1 for every key being pressed
      if rotorCLetter == rotorCNotch:
        rotorTrigger = True
      rotorCLetter = alphabet[(alphabet.index(rotorCLetter) + 1) % 26]
      #Check if rotorB needs to rotate
      if rotorTrigger:
        rotorTrigger = False
        if rotorBLetter == rotorBNotch:
          rotorTrigger = True
        rotorBLetter = alphabet[(alphabet.index(rotorBLetter) + 1) % 26]

        #Check if rotorA needs to rotate
        if (rotorTrigger):
          rotorTrigger = False
          rotorALetter = alphabet[(alphabet.index(rotorALetter) + 1) % 26]

      else:
          #Check for double step sequence!
        if rotorBLetter == rotorBNotch:
          rotorBLetter = alphabet[(alphabet.index(rotorBLetter) + 1) % 26]
          rotorALetter = alphabet[(alphabet.index(rotorALetter) + 1) % 26]

      #Implement plugboard encryption!
      if letter in plugboardDict.keys():
        if plugboardDict[letter]!="":
          encryptedLetter = plugboardDict[letter]

      #Rotors & Reflector Encryption
      offsetA = alphabet.index(rotorALetter)
      offsetB = alphabet.index(rotorBLetter)
      offsetC = alphabet.index(rotorCLetter)

      # Wheel 3 Encryption
      pos = alphabet.index(encryptedLetter)
      let = rotorC[(pos + offsetC)%26]
      pos = alphabet.index(let)
      encryptedLetter = alphabet[(pos - offsetC +26)%26]

      # Wheel 2 Encryption
      pos = alphabet.index(encryptedLetter)
      let = rotorB[(pos + offsetB)%26]
      pos = alphabet.index(let)
      encryptedLetter = alphabet[(pos - offsetB +26)%26]

      # Wheel 1 Encryption
      pos = alphabet.index(encryptedLetter)
      let = rotorA[(pos + offsetA)%26]
      pos = alphabet.index(let)
      encryptedLetter = alphabet[(pos - offsetA +26)%26]

      # Reflector encryption!
      if encryptedLetter in reflectorDict.keys():
        if reflectorDict[encryptedLetter]!="":
          encryptedLetter = reflectorDict[encryptedLetter]

      #Back through the rotors
      # Wheel 1 Encryption
      pos = alphabet.index(encryptedLetter)
      let = alphabet[(pos + offsetA)%26]
      pos = rotorA.index(let)
      encryptedLetter = alphabet[(pos - offsetA +26)%26]

      # Wheel 2 Encryption
      pos = alphabet.index(encryptedLetter)
      let = alphabet[(pos + offsetB)%26]
      pos = rotorB.index(let)
      encryptedLetter = alphabet[(pos - offsetB +26)%26]

      # Wheel 3 Encryption
      pos = alphabet.index(encryptedLetter)
      let = alphabet[(pos + offsetC)%26]
      pos = rotorC.index(let)
      encryptedLetter = alphabet[(pos - offsetC +26)%26]

      #Implement plugboard encryption!
      if encryptedLetter in plugboardDict.keys():
        if plugboardDict[encryptedLetter]!="":
          encryptedLetter = plugboardDict[encryptedLetter]

    ciphertext = ciphertext + encryptedLetter

  return ciphertext



button_clicks = []


#   Setting up master password displat

def firstTimeScreen():
    window.geometry("250x150")
    
    lbl = Label(window, text="Create Master Password")
    lbl.config(anchor=CENTER)
    lbl.pack()

    txt = Entry(window, width=20, show="*")
    txt.pack()
    txt.focus()

    lbl1 = Label(window, text="Re-enter Password")
    lbl1.config(anchor=CENTER)
    lbl1.pack()

    txt1 = Entry(window, width=20, show="*")
    txt1.pack()

    # Check which encryption is chosen
    def Caesar_clicked():
        global button_clicks
        button_clicks.append("Caesar")

    def UTF_clicked():
        global button_clicks
        button_clicks.append("UTF")

    def Enigma_clicked():
        global button_clicks
        button_clicks.append("Enigma")
        

    # Saving Password after encryptions
    def savePassword_UTF():
        if txt.get() == txt1.get():
            hashedPassword = UTF_encrypt(txt.get().encode('utf-8'))
            insert_password = """INSERT INTO masterpassword(password)
            VALUES(?) """
            cursor.execute(insert_password, [hashedPassword])
            UTF_clicked()
            db.commit()
            vaultScreen()

        else:
            lbl.config(text="Passwords don't match")


    def savePassword_Caesar():
        if txt.get() == txt1.get():
            
            hashedPassword = Caesar_encrypt(txt.get())
            insert_password = """INSERT INTO masterpassword(password)
            VALUES(?) """
            cursor.execute(insert_password, [hashedPassword])
            Caesar_clicked()
            db.commit()
            vaultScreen()

        else:
            lbl.config(text="Passwords don't match")

    def savePassword_Enigma():
        if txt.get() == txt1.get():
            hashedPassword = Enigma_encrypt(txt.get())
            insert_password = """INSERT INTO masterpassword(password)
            VALUES(?) """
            cursor.execute(insert_password, [hashedPassword])
            Enigma_clicked()
            db.commit()
            vaultScreen()

        else:
            lbl.config(text="Passwords don't match")


    btn = Button(window, text="Save with Enigma encode", command=savePassword_Enigma)
    btn.pack(pady=5)

    

    




#   Login screen display

def loginScreen():
    window.geometry("500x125")
    

    lbl = Label(window, text="Enter Master Password", font='Helvetica 35 bold')
    lbl.pack()

    txt = Entry(window, width=20, show="*")
    txt.pack()
    txt.focus()
 

    def getMasterPassword():
        global button_clicks
        if button_clicks=="Caesar":
            checkhashedpassword = Caesar_encrypt(txt.get())


        elif button_clicks=="UTF":
            checkhashedpassword = UTF_encrypt(txt.get())

        else:

            checkhashedpassword = Enigma_encrypt(txt.get())


        cursor.execute("SELECT * FROM masterpassword WHERE id = 1 AND password = ?", [checkhashedpassword])
        return cursor.fetchall()

    def checkPassword():
        password = getMasterPassword()

        if password:
            vaultScreen()

        else:
            txt.delete(0, 'end')
            lbl.config(text="Wrong Password")

    btn = Button(window, text="Submit", command=checkPassword)
    btn.pack(pady=5)






encryption_type=[]

#   Vault Menu functions

def vaultScreen():
    for widget in window.winfo_children():
        widget.destroy()

    def Caesar_clicked():
        global encryption_type
        encryption_type.append("Caesar")

    def UTF_clicked():
        global encryption_type
        encryption_type.append("UTF")

    def Enigma_clicked():
        global encryption_type
        encryption_type.append("Enigma")

    

    def addEntry():
        text1 = "Platform"
        text2 = "Username"
        text3 = "Password"

        platform = popUp(text1)
        account = popUp(text2)
        password = popUp(text3)
        
        #PASSWORD=ENCRYPT(POPUP) AND THEN INSERT

        insert_fields = """INSERT INTO vault(platform, account, password)
        VALUES(?, ?, ?)"""

        cursor.execute(insert_fields, (platform, account, password))
        db.commit()
        vaultScreen()

    def updateEntry(input):
        update = "Type new password"
        password = popUp(update) 

        cursor.execute("UPDATE vault SET password = ? WHERE id = ?", (password, input,))
        db.commit()
        vaultScreen()

    def removeEntry(input):
        cursor.execute("DELETE FROM vault WHERE id = ?", (input,))
        db.commit()
        vaultScreen()

    def copyAcc(input):
        window.clipboard_clear()
        window.clipboard_append(input)

    def copyPass(input):
        window.clipboard_clear()
        window.clipboard_append(input)

    def searchCredentials():
        text1 = "Enter platform (URL)"
        text2 = "Enter account (username)"

        platform = popUp(text1)
        account = popUp(text2)

        cursor.execute("SELECT * FROM vault WHERE platform = ? AND account = ?", (platform, account))

        credentials = cursor.fetchall()

        if credentials:
            text = f"Platform: {credentials[0][1]}\nAccount: {credentials[0][2]}\nPassword: {credentials[0][3]}"
            popUp_button(text, credentials[0][3])
        else:
            popUp_button("Credentials not found", "")

    def chooseEncryption():
        window = Tk()
        

        window.title("Encryption")

        myFrame = Frame(window)
        myFrame.pack(pady=20)

        lbl = Label(myFrame, text="Choose Encryption Method", font='Helvetica 25 bold')
        lbl.grid(row=0,column=1)

    
        myButton = Button(myFrame, text="Caesar",command=Caesar_clicked())
        myButton.grid(row=1, column=0, padx=10)

        myButton1 = Button(myFrame, text="UTF", command=UTF_clicked())
        myButton1.grid(row=1, column=1, padx=10)

        myButton2 = Button(myFrame, text="ENIGMA",command=Enigma_clicked())
        myButton2.grid(row=1, column=2, padx=10)

        myFrame = Frame(window)
        myFrame.pack(pady=20)
        print(encryption_type)
        window.mainloop()

#   Window layout 

    window.geometry("1400x300")
    main_frame = Frame(window)
    main_frame.pack(fill=BOTH, expand=5)

    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=5)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    second_frame = Frame(my_canvas)

    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

    lbl = Label(second_frame, text="Password Watch Tower", font='Helvetica 35 bold')
    lbl.grid(column=1)
    
    choose = Button(second_frame, text="Choose Encryption method",command=chooseEncryption)
    choose.grid(column=1,padx=10)

    btn2 = Button(second_frame, text="Auto - Generate Password", command=passGenerator)
    btn2.grid(row=2,column=6, pady=10)

    search_btn = Button(second_frame, text="Search Credential", command=searchCredentials)
    search_btn.grid(row=2, column=5, pady=10)

    btn = Button(second_frame, text="Store New Credentials", command=addEntry)
    btn.grid(row=2, column=4, pady=10)

    lbl = Label(second_frame, text="Platform", font='Helvetica 20 bold')
    lbl.grid(row=2, column=0, padx=40)
    lbl = Label(second_frame, text="Username", font='Helvetica 20 bold')
    lbl.grid(row=2, column=1, padx=40)
    lbl = Label(second_frame, text="Password", font='Helvetica 20 bold')
    lbl.grid(row=2, column=2, padx=40)

    cursor.execute("SELECT * FROM vault")


#   Buttons Layout

    show_buttons = [] # create a list to store the Show/Hide buttons
    if cursor.fetchall() is not None:
        i = 0
        while True:
            cursor.execute("SELECT * FROM vault")
            array = cursor.fetchall()


            def showPassword(password, lbl3, idx):
                show_btn = show_buttons[idx] # get the corresponding Show/Hide button
                if password == '':
                    lbl3.configure(text=len(password)*"*")
                elif show_btn['text'] == 'Show':
                    lbl3.configure(text=password)
                    show_btn.configure(text='Hide')
                else:
                    lbl3.configure(text=len(password)*"*")
                    show_btn.configure(text='Show')


            lbl1 = Label(second_frame, text=(array[i][1]))
            lbl1.grid(column=0, row=i + 3)
            lbl2 = Label(second_frame, text=(array[i][2]))
            lbl2.grid(column=1, row=i + 3)
            lbl3 = Label(second_frame, text=len(array[i][3])*"*")
            lbl3.grid(column=2, row=i + 3)
            btn2 = Button(second_frame, text="Copy Username", command=partial(copyAcc, array[i][2]))
            btn2.grid(column=4, row=i + 3, pady=10)
            btn3 = Button(second_frame, text="Copy Password", command=partial(copyPass, array[i][3]))
            btn3.grid(column=5, row=i + 3, pady=10)
            btn1 = Button(second_frame, text="Update Password", command=partial(updateEntry, array[i][0]))
            btn1.grid(column=6, row=i + 3, pady=10)
            btn = Button(second_frame, text="Delete", command=partial(removeEntry, array[i][0]))
            btn.grid(column=7, row=i + 3, pady=10)
            show_btn = Button(second_frame, text="Show", command=partial(showPassword, array[i][3], lbl3, i))
            show_btn.grid(column=3, row=i+3, pady=10)
            show_buttons.append(show_btn) # add the button to the list

            i = i + 1
                                                                             
                                                                        

            cursor.execute("SELECT * FROM vault")
            if len(cursor.fetchall()) <= i:
                break

cursor.execute("SELECT * FROM masterpassword")
if cursor.fetchall():
    loginScreen()
else:
    firstTimeScreen()
window.mainloop()
