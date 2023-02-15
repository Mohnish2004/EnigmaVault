#passwordchecker.py
#Enigma - Ryan Ffrench
#
#Checks if your password is secure
#Note:
#Can easily modify the criteria used to check password security. I was unsure exactly what the criteria should be.

def main():
    password = input("Enter password:") # Asks for the password

    password_length = len(password) #Determines length of password

    # sets a variety of iteration variables to 0 
    lowercase = 0
    uppercase = 0
    num = 0
    special = 0
    score = 0 # used as a number grade
    grade = 0 # used to give meaning to the score

    for character in password:
        if character.islower(): # checks each character in the password if lowercase 1 is added to the variables value
            lowercase = lowercase + 1
        if character.isupper(): # checks each character in the password if uppercase 1 is added to the variables value
            uppercase = uppercase + 1
        if character.isdigit(): # checks each character in the password if a number 1 is added to the variables value
            num = num + 1
        if character in "'@#$?%^&()_-*!":  # checks each character in the password if a special character 1 is added to the variables value
            special = special + 1
        
    #print("Length:", password_length) # prints the length of the password !!Commented out for now idk if its needed


    # if any of the variables are equal to 1 or more then the password entered has the element in it.
    if lowercase > 0: 
        score = score + 1 
        lowercaseMiss = None
    else:
        print("Missing a lowercase letter!")
    if uppercase > 0:
        score = score + 1
    else:
        print("Missing an uppercase letter!")
    if num > 0:
        score = score + 1
    else:
         print("Missing a number!")
    if special > 0:
        score = score + 1
        specialMiss = None
    else:
        print("Missing a special character!")
    if password_length > 8: 
        score = score + 2
    else:
        print("Password should be longer than 8 characters!")

    #Catagorizes passwords into Strong, Intermediate, and Weak (can be changed easily to add more criteria or anything really)
    if score == 5:
        grade = "Strong!"
    if score == 4:
        grade = "Could be Stronger!"
    if score < 4:
        grade = "Weak!"


    #print(f"{score*2}/10") #decided against this as there is really no point
    print(grade)

main()
        
