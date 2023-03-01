# Enigma-Vault
GDSC PROJECT
Enigma Vault
This is a Python script for a password manager called Enigma Vault. It allows the user to store different passwords for different accounts and platforms. It uses SQLite3 to store the passwords in a database and provides a GUI interface created with the tkinter module.

Installation
To run this script, you need to install the following dependencies:

Python 3
tkinter module
passgen module
The tkinter module should come pre-installed with Python 3. For installing the passgen module, run the following command in your terminal:

bash
Copy code
pip install passgen
Usage
After installing the dependencies, you can run the script by executing the following command in your terminal:

bash
Copy code
python enigma_vault.py
The Enigma Vault GUI will appear on your screen. You can start by creating a master password, which will be used to encrypt all other passwords stored in the database. After creating the master password, you can add new accounts and platforms along with their respective passwords. You can also view the stored passwords and copy them to your clipboard by clicking the 'Copy Password' button.

How it works
Enigma Vault encrypts the user's passwords using various encryption methods like MD5, Caesar Cipher, and Enigma Machine. The master password is first encrypted using MD5 and then again encrypted using Caesar Cipher. The Enigma Machine is used to encrypt the other passwords stored in the database. The different settings for the Enigma Machine like the rotors, reflectors, ring settings, and ring positions can be customized by the user.

The passwords are stored in a SQLite3 database with two tables - 'masterpassword' and 'vault'. The 'masterpassword' table stores the encrypted master password, while the 'vault' table stores the encrypted passwords for the different accounts and platforms.
