# import the Tkinter and ttk libraries, and the os and random modules
from tkinter import *
from tkinter import ttk
import os
import random
from tkinter import filedialog

# define a function to encrypt a message using a substitution cipher


# define a function to encrypt a message using a substitution cipher
def encrypt(message, key):
    # create a list of the alphabet
    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    # randomly shuffle the alphabet
    random.shuffle(alphabet)

    # create the key by joining the shuffled alphabet into a string
    key = "".join(alphabet)

    # create a new empty string for the encrypted message
    encrypted = ""

    # loop through each character in the message
    for char in message:
        # check if the character is a letter
        if char.lower() in alphabet:
            # encrypt the letter by substituting it with the corresponding letter in the key
            encrypted += key[alphabet.index(char.lower())]
        else:
            # if the character is not a letter, add it to the encrypted message without encrypting it
            encrypted += char

    # return the encrypted message
    return encrypted

# define a function to decrypt a message using a substitution cipher


def decrypt(message, key):
    # create a list of the alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # create a new empty string for the decrypted message
    decrypted = ""

    # loop through each character in the message
    for char in message:
        # check if the character is a letter
        if char.lower() in alphabet:
            # decrypt the letter by substituting it with the corresponding letter in the alphabet
            decrypted += alphabet[key.index(char.lower())]
        else:
            # if the character is not a letter, add it to the decrypted message without decrypting it
            decrypted += char

    # return the decrypted message
    return decrypted

# define a function to handle button clicks

# define a function to handle button clicks


def button_click(action):
    # get the message and key from the input fields
    message = input_field.get()
    key = key_field.get()

    # check which button was clicked
    if action == "Encrypt":
        # encrypt the message
        output = encrypt(message, key)
    elif action == "Decrypt":
        # decrypt the message
        output = decrypt(message, key)
    elif action == "Save":
        # prompt the user to select a file to save the message to
        file = filedialog.asksaveasfilename()

        # check if the user selected a file
        if file:
            # save the message to the file
            with open(file, "w") as f:
                f.write(output_field.get())
    elif action == "Load":
        # prompt the user to select a file to load the message from
        file = filedialog.askopenfilename()

        # check if the user selected a file
        if file:
            # load the message from the file
            with open(file, "r") as f:
                message = f.read()

            # update the input field with the loaded message
            input_field.delete(0, END)
            input_field.insert(0, message)
    elif action == "Generate Key":
        # create a list of the alphabet
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        # create a new empty string for the key
        key = ""

        # randomly shuffle the alphabet
        random.shuffle(alphabet)

        # create the key by joining the shuffled alphabet into a string
        key = "".join(alphabet)

        # update the key field with the generated key
        key_field.delete(0, END)
        key_field.insert(0, key)

    # update the output field with the encrypted or decrypted message
    output_field.delete(0, END)
    output_field.insert(0, output)


# create a new Tkinter window
window = Tk()

# set the window title
window.title("Substitution Cipher")

# create a ttk.Label for the input field
input_label = ttk.Label(window, text="Message:")
input_label.grid(row=0, column=0, padx=5, pady=5, sticky="W")

# create a ttk.Entry field for the input
input_field = ttk.Entry(window, width=40)
input_field.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

# create a ttk.Label for the key field
key_label = ttk.Label(window, text="Key:")
key_label.grid(row=1, column=0, padx=5, pady=5, sticky="W")

# create a ttk.Entry field for the key
key_field = ttk.Entry(window, width=40)
key_field.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

# create a ttk.Button for encrypting the message
encrypt_button = ttk.Button(window, text="Encrypt",
                            command=lambda: button_click("Encrypt"))
encrypt_button.grid(row=2, column=1, padx=5, pady=5)

# create a ttk.Button for decrypting the message
decrypt_button = ttk.Button(window, text="Decrypt",
                            command=lambda: button_click("Decrypt"))
decrypt_button.grid(row=2, column=2, padx=5, pady=5)

# create a ttk.Button for saving the message
save_button = ttk.Button(
    window, text="Save", command=lambda: button_click("Save"))
save_button.grid(row=3, column=1, padx=5, pady=5)

# create a ttk.Button for loading a message
load_button = ttk.Button(
    window, text="Load", command=lambda: button_click("Load"))
load_button.grid(row=3, column=2, padx=5, pady=5)

# create a ttk.Button for loading a message
load_button = ttk.Button(
    window, text="Load", command=lambda: button_click("Load"))
load_button.grid(row=3, column=2, padx=5, pady=5)

# create a ttk.Button for generating a key
generate_button = ttk.Button(
    window, text="Generate Key", command=lambda: button_click("Generate Key"))
generate_button.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

# create a ttk.Label for the output field
output_label = ttk.Label(window, text="Output:")
output_label.grid(row=5, column=0, padx=5, pady=5, sticky="W")

# create a ttk.Entry field for the output
output_field = ttk.Entry(window, width=40)
output_field.grid(row=5, column=1, columnspan=2, padx=5, pady=5)

# create a ttk.Separator to separate the input and output fields
separator = ttk.Separator(window, orient=HORIZONTAL)
separator.grid(row=6, column=0, columnspan=3, sticky="EW", pady=5)

# run the main event loop
window.mainloop()
