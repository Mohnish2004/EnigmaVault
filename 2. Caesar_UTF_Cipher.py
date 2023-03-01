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


