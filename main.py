'''def encrypt(data,shift):
    encrypted=""
    for i in range (len(data)):
        char = data[i]
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

def decrypt(data,shift):
    decrypted=""
    for i in range(len(data)):
        char = data[i]z
        if (char.isupper()):
            decrypted += chr((ord(char)-shift -65)% 26 + 65)
        elif (char.islower()):
            decrypted += chr((ord(char)-shift - 97) % 26 + 97)
        elif (char.isdigit()):
            number = (int(char)-shift) % 10
            decrypted += str(number)
        else:
            decrypted += char
    return decrypted

choice=0
while choice != '1' or choice !='2':
    menu = input()

    if menu =='1':
        Website_Name = input("enter the name of the website ")
        User_Name = input("enter the username ")
        Password = input("enter the password ")
        file = open("vault.txt","a")
        shift=5
        file.write(encrypt(Website_Name,shift)+"{|}"+encrypt(User_Name,shift)+"{|}"+encrypt(Password,shift)+"\n")
        file.close()

    if menu =='2':
        file = open("vault.txt","r")
        print("Website\t\tUsername\tPassword")
        shift =5 
        for i in file:
            data = i.split("{|}")
            print(decrypt(data[0],shift)+"\t\t"+decrypt(data[1],shift)+"\t"+"*"*(len(data[2])-1))
        print("do you want to reveal the passwords")
        a=input("yes/no")
        print("Website\t\tUsername\tPassword")
        if a=="yes":
            file.seek(0)
            for i in file:
                data = i.split("{|}")
                print(decrypt(data[0],shift)+"\t\t"+decrypt(data[1],shift)+"\t"+decrypt(data[2],shift))
            


    if menu =='3':
        exit()
'''
class Credentials:
    def __init__(self, website, username, password):
        self.website = website
        self.username = username
        self.password = password
        self.shift = 5

    def encrypt(self, data):
        encrypted = ""
        for i in range(len(data)):
            char = data[i]
            if (char.isupper()):
                encrypted += chr((ord(char) + self.shift - 65) % 26 + 65)
            elif (char.islower()):
                encrypted += chr((ord(char) + self.shift - 97) % 26 + 97)
            elif (char.isdigit()):
                number = (int(char) + self.shift) % 10
                encrypted += str(number)
            else:
                encrypted += char
        return encrypted

    def decrypt(self, data):
        decrypted = ""
        for i in range(len(data)):
            char = data[i]
            if (char.isupper()):
                decrypted += chr((ord(char) - self.shift - 65) % 26 + 65)
            elif (char.islower()):
                decrypted += chr((ord(char) - self.shift - 97) % 26 + 97)
            elif (char.isdigit()):
                number = (int(char) - self.shift) % 10
                decrypted += str(number)
            else:
                decrypted += char
        return decrypted

    def write_to_file(self):
        file = open("vault.txt", "a")
        file.write(self.encrypt(self.website) + "{|}" + self.encrypt(self.username) + "{|}" + self.encrypt(self.password) + "\n")
        file.close()

    def read_from_file(self):
        print("Website\t\tUsername\tPassword")
        with open("vault.txt", "r") as file:
            for line in file:
                data = line.strip().split("{|}")
                print(self.decrypt(data[0]) + "\t\t" + self.decrypt(data[1]) + "\t" + "*" * (len(data[2]) - 1))

    def menu(self):
        choice = 0
        while choice != '1' or choice != '2':
            print('''What would you like to do
                      1. Input new credentials
                      2. View old credentials
                      3. quit''')
            choice = input()
            if choice == '1':
                website_name = input("Enter the name of the website: ")
                username = input("Enter the username: ")
                password = input("Enter the password: ")
                cred = Credentials(website_name, username, password)
                cred.write_to_file()
            elif choice == '2':
                self.read_from_file()
                reveal_pass = input("Do you want to reveal the password? (y/n): ")
                if reveal_pass == 'y':
                    with open("vault.txt", "r") as file:
                        for line in file:
                            data = line.strip().split("{|}")
                            print(self.decrypt(data[0]) + "\t\t" + self.decrypt(data[1]) + "\t" + self.decrypt(data[2]))
            elif choice == '3':
                break
            else:
                print("Invalid input")


cred = Credentials("", "", "")
cred.menu()

