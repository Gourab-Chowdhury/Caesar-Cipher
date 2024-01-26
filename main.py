alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)



'''
#Creating a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):  
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")

#Creating a function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_text, shift_amount):
  plain_text = ""
  for letter in cipher_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    plain_text += alphabet[new_position]
  print(f"The decoded text is {plain_text}")

#Calling the encrypt & decrypt function and pass in the user inputs.
if direction == "encode":
  encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
  decrypt(cipher_text=text, shift_amount=shift)

'''


#Combine the encrypt() and decrypt() functions into a single function called caesar().

#Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

def caesar(start_text, shift_amount, cipher_direction): 
  final_text = ""
  #for letter in start_text:
  for char in start_text:
    if char in alphabet: 
       position = alphabet.index(char)
       if cipher_direction == "encode":  
          new_position = position + shift_amount
          final_text += alphabet[new_position]
       elif cipher_direction == "decode":
          new_position = position - shift_amount
          final_text += alphabet[new_position]
    else:
      final_text = final_text + char
  print(f"The {cipher_direction}d text is '{final_text}' ")

continue_program = True
while continue_program:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  caesar(start_text = text, shift_amount = shift, cipher_direction = direction)
  result =  input("Type 'yes' if you continue this program or 'no': ")

  if result == 'no':
    continue_program = False
    print("Good Bye.")
