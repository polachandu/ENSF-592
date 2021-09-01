# encryption.py
# AUTHOR NAME: Chandrahas_Reddy_Pola
#
# A terminal-based encryption application capable of both encoding and decoding text when given a specific cipher.
# Detailed specifications are provided via the Assignment 3 git repository.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.

# import re for using regular expressions
#inport string for using ascii_lowercase used in cipher function
import re
import string
#define class encryption_decryption
class EncryptionDecryption :
    @staticmethod
    def assignment():
    #choice function is defined to choose whether the user to use encode or decode
    #take input as 1 or 2 if not those two it prompts again by messaging you must either select 1 or 2
    #no return value
        def choice(): 
            while True:  
                choice=str(input("Select 1 to encode or 2 to decode your message : "))
                if choice == "1":
                    return choice
                elif choice == "2":
                    return choice
                else:
                    print("you must either select 1 or 2")
                    #return choice()
    #defined text function to enter the input text without punctuation and spaces. The output should be in lower case letter so converting input to lower case letters
    #no parameters
    # it take input as string 
    #it returns message with lowercase and without punctuation and spaces
        def text():
            message = input("Please enter the text to be processed: ")
            message1 = re.sub('[^A-Za-z0-9]+', '', message)
            message2 = message1.lower()
            print(message2)
            return message2
    #defined cipher function
    #It takes no parameters
    #It takes input as string and converts it into without space,puctuation and in lower case. 
    #It returns the ciphertext if input is 26 letters
    #If not 26 it throws error and prompts to input the cipher again
        
        def cipher():
            a = list(string.ascii_lowercase)
            a.extend(['0','1','2','3','4','5','6','7','8','9'])
            while True:
                ciphertext = input("Please enter the cipher text: ")
                try:
                    if len(ciphertext)==26 and all(elem in a for elem in list(ciphertext)) :
                            return ciphertext
                    else:
                        raise ValueError("Enter the valid 26 letter cipher and it should be lower case")
                except ValueError:
                    print("Enter the valid 26 letter cipher and it should be lower case")
                    return cipher()
                    
            
                        
    #defined coded funtion
    # It takes parameters as choice, text and cipher
    # It returns the translated encoded or decoded string       
        def coded(choice,text,cipher):
            translated =""
            cipher = list(cipher)
            if choice == "2":
                for charachter in text:
                    num = cipher.index(charachter)
                    translated+=chr(num+97)
                return translated
            elif choice== "1":
                for charachter in text:
                    num=ord(charachter) - 97
                    translated+=cipher[num]
                return translated
        choice = choice()
        text = text()
        cipher = cipher()
        final = coded(choice,text,cipher)
        return final




# defined main class and it just calls the above class with function
#It displays the output
class main:
    output = EncryptionDecryption.assignment()
    print("Your output is: ",output)
    
