alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(plain_text, shift_amount, cipher_direction):
  cipher_text = ""
  for letter in text:
    if direction == "encode":
        if letter in alphabet:
              new_position = alphabet.index(letter) + shift
              cipher_text += alphabet[new_position]
        else:
              cipher_text += letter
    elif direction == "decode":
        if letter in alphabet:
              new_position = alphabet.index(letter) - shift
              cipher_text += alphabet[new_position]
        else:
              cipher_text += letter
          
  print(f"The encoded text is:\n{cipher_text}")
    #TODO-3: What happens if the user enters a number/symbol/space?
  
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    

#TODO-1: Import and print the logo from art.py when the program starts.

from art import logo
print(logo)

#TODO-4: Can you figu re out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(plain_text=text, shift_amount=shift, cipher_direction=direction)

    result = input('Type "yes" if you want to go again. Otherwise type "no".\n')
    if result == "yes":
      continue
    elif result == "no":
      should_continue = False
    break
print('Goodbye!')
   
  
  