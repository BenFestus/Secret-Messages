'''SECRET MESSAGES'''

from secrets import choice
from tkinter import Tk, messagebox, simpledialog


def get_task():
    #Opens dialog box
    task = simpledialog.askstring('Task', 'Type encrypt or decrypt ')
    return task #Passing value of task back to function

def get_secret_message():
    user_message = simpledialog.askstring('PICKER', 'Type secret message')
    return user_message

def is_odd(number):
    return number % 2 == 1 #Passing odd numbers to function

def get_odd_letters(message):
    #List holds odd letters 
    odd_letters = []

    for counter in range(0, len(message)):
        if is_odd(counter):
            #When counter is odd, append a letter in message to odd letters list
            odd_letters.append(message[counter])
    return odd_letters

def encrypt_message(message):
    #List holds letters from message and fake letters
    encrypted_list = []
    
    fake_letters = ['a', 'b', 'f', 's', 't', 'k', 'v', 'w']
    for counter in range(0, len(message)):
        #Add fake letter to encrypted list
        encrypted_list.append(choice(fake_letters))
        #Add a letter from message to encrypted list
        encrypted_list.append(message[counter])
    
    #Joins the letter in encrypted list into a string
    encrypted_message = ''.join(encrypted_list)
    return encrypted_message

def decrypt_message(message):
    odd_letters = get_odd_letters(message)
    decrypted_message = ''.join(odd_letters)
    return decrypted_message

def display_encrypt(message):
    messagebox.showinfo('Encrypt', 'Encrypted message is ' + message)

def display_decrypt(message):
    messagebox.showinfo('Decrypt', 'Decrypted message is ' + message)


while True:
    #Get task to perform from user
    task = get_task()
    if task == 'encrypt':
        #Get secret message
        user_message = get_secret_message()
        #Encrypte secret message
        encrypted_message = encrypt_message(user_message)
        #Display encrypted message
        display_encrypt(encrypted_message)

    elif task== 'decrypt':
        user_message = get_secret_message()
        decrypted_message = decrypt_message(user_message)
        display_decrypt(decrypted_message)
    
    else:
        break

    