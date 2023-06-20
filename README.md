![Screen_Shot_2023-02-28_at_11 38 39_PM-removebg-preview](https://user-images.githubusercontent.com/81405395/222884977-f13715de-67ba-463b-a6b8-fdbb57b5f3f9.png)

https://user-images.githubusercontent.com/81405395/222273422-bcaaaaf6-2e52-426f-b6ff-b0151a2a414d.mov


# Enigma Vault

Enigma Vault is a secure local password manager that uses multiple encryption techniques to protect your login information. It features Caesar encryption, UTF-8 encoding, and Enigma encryption, with AES/DES/RSA coming soon. By utilizing these encryption methods, Enigma Vault offers a high level of security for your sensitive data while also educating users about these cipher techniques. With Enigma Vault, you can store and manage all your passwords with peace of mind.


# Basic Features 

*Securely store your passwords and login information with Enigma Vault, a local password manager that offers a high level of security for your sensitive data.

* Generate strong, random passwords using the passGenerator library, which saves you time and ensures that your passwords are difficult to guess.

* Encrypt your master password using multiple encryption techniques, including Caesar encryption, UTF-8 encoding, and Enigma encryption, with AES/DES/RSA coming soon.

* Enigma encryption, one of the encryption techniques used by Enigma Vault, was inspired by the famous Enigma machine used by the Germans during World War II. This machine was famously cracked by Alan Turing and his team, as depicted in the movie "The Imitation Game".

* Enjoy a range of features, including show/hide passwords, add/delete/update/search credentials, and copy-to-clipboard, that make password management easy and convenient.

## Installation

### Need to add clone repository instructions sometime in the future....

This document outlines the requirements for a Python application that will make use of the following modules:

hashlib, sqlite3, functools, tkinter, passgen

```python
import hashlib
import sqlite3
from functools import partial
from tkinter import *
from tkinter import simpledialog
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
```

## User Interface
The user interface will be implemented using the tkinter module. The application will have the following components:

>Master Password setup: This window will be shown the first time, and you need to remember this password for the next logins 

>Login window: This window will prompt the user for the master password

>Main window: This window will display a list of stored passwords and allow the user to add, edit, delete passwords and other functions

>Add credential dialog: This dialog will allow the user to add a new password to the database.

>Update password dialog: This dialog will allow the user to edit an existing password in the database.

>Generate password dialog: This dialog will allow the user to generate a strong, random password using the passgen module.

## Usage

Enter your master password to unlock the password vault

Add new entries to the password vault using the GUI

Edit or delete existing entries as needed

Use the copy button to copy a password to the clipboard

Coming soon...


## Contributing

![Team Engima](https://user-images.githubusercontent.com/81405395/222884906-71ea2f17-2d8f-4699-a631-2eb903ee2ea4.png)

Presentations - https://www.canva.com/design/DAFb6gjbVCU/0KLLIe2q4y1NRNW95OznQQ/edit?utm_content=DAFb6gjbVCU&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

## License

License
This project is licensed under the MIT License. See the LICENSE file for details.

[MIT](https://choosealicense.com/licenses/mit/)
