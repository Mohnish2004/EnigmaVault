#passwordgenerator.py
#Enigma - Ryan Ffrench
#
#Generates a password based off user defined parameters.

import random #used to generate the random characters in the password
import string #used to specify the range of values that the rand function should choose from
import time #used to make the psuedo random numbers more random. I think the rand module is fine for this, but could look into alternatives if needed

random.seed(time.time()) #seeds the random function

def scramble(tempstring): #takes the strings of random characters/numbers generated and scrambles them together
    templist = list(tempstring)
    random.shuffle(templist)
    final = ''.join(templist)
    return final

#will only add comments for this function because all the ones below work the same way 
def specialchars(numSpecialchars): #Generates random special characters
    randspecial = '' # defines an empty string
    for _ in range(numSpecialchars): #Loops for the number the user enters when asked for the number of special characters
        random_letter = random.choice('@#$?%^&()_-*!') #picks one of these special characters
        randspecial += random_letter # adds to the empty string
    return randspecial #returns string

    
def regularchars(numRegularchars): #Generates random letters uppercase & lowercase. If needed this function could be split into lower and uppercase
    randchars = ''
    for _ in range(numRegularchars):
        random_letter = random.choice(string.ascii_letters) #string.ascii_letters as the name implies is all the letters in the english alphabet upper & lowercase
        randchars += random_letter
    return randchars

    

def numbers(numNumbers):
    randnum = ''
    for _ in range(numNumbers):
        random_letter = random.choice(string.digits) #string.digits picks from 0 - 9 
        randnum += random_letter
    return randnum



def main ():
    while True: 
        while True: # for input validation I just used try & except statements. Could probably be simplified, but this was what came to mind
            # loops until the user enters valid input 
            try:
                numLength = input("How long would you like your password to be?:")
                numLength = int(numLength) #if the user enters a number that is not an integer there will be an error, so the except block will be executed
                break
            except:
                print("Please enter a whole number or q to quit") #If the user wants to quit they can enter Q or q
                if numLength == 'q' or numLength == 'Q':
                    exit(0) 
                else:
                    continue # loops until the user gives correct input 
                continue
        while True:
            try:
                numNumbers = input("How many numbers?:")
                numNumbers = float(numNumbers)
                numNumbers = int(numNumbers)
                break
            except:
                print("Please enter a whole number or q to quit")
                if numNumbers == 'q' or numNumbers == 'Q':
                    exit(0)
                else:
                    continue
                continue
        while True:
            try:
                numSpecialchars = input("How many special characters ('@#$?%^&()_-*!)?:")    
                numSpecialchars = int(numSpecialchars)
                break
            except:
                print("Please enter a whole number or q to quit")
                if numNumber == 'q' or numNumber == 'Q':
                    exit(0)
                else:
                    continue
                continue
        if numLength - (numSpecialchars + numNumbers) >= 0: #if the user wants a password that has more numbers & special chars than desired length an error is thrown
            numRegularchars = numLength - (numSpecialchars + numNumbers)
            break
        else: 
            print("Error: Password Length must be at least equal to the desired number of special characters + the desired number of numbers") 
            print("Try again or enter q to quit")
            
    #Calls functions and assigns a variable to each returned string      
    finSpecialchars = specialchars(numSpecialchars) 
    finRegularchars = regularchars(numRegularchars)
    finNumbers = numbers(numNumbers)
    tempstring = finRegularchars + finSpecialchars + finNumbers #Makes one string isn't python nice :0
    finPass = scramble(tempstring)
    print(finPass) # prints password
    
main()
